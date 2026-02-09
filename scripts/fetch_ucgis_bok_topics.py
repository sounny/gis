import argparse
import concurrent.futures
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional, Dict, Any


DEFAULT_BASE = "https://ucgis-bok-default-rtdb.firebaseio.com"


def _http_get_json(url: str, timeout_s: int = 60, retries: int = 4) -> object:
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "gis-bok-export/1.0"})
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                data = resp.read()
            return json.loads(data.decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
            last_err = e
            # exponential backoff
            time.sleep(1.5 ** attempt)
    raise RuntimeError(f"GET failed after {retries} attempts: {url}\n{last_err}")


_SAFE_NAME_RE = re.compile(r"[^A-Za-z0-9._-]+")


def _safe_filename(s: str) -> str:
    s = (s or "").strip()
    s = s.replace(" ", "-")
    s = _SAFE_NAME_RE.sub("-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "topic"


def _write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def _write_json(path: str, obj: object) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=True, indent=2, sort_keys=True)
        f.write("\n")


def _topic_to_markdown(topic: dict) -> str:
    # Keep source HTML intact (BoK text often includes inline figures/abbr tags).
    code = topic.get("code", "")
    name = topic.get("name", "")
    link = topic.get("link", "")

    def sec(title: str, key: str) -> str:
        val = topic.get(key)
        if not val:
            return ""
        return f"\n## {title}\n\n{val}\n"

    out = []
    out.append(f"# {code} - {name}".strip())
    if link:
        out.append("")
        out.append(f"Source: {link}")
    out.append(sec("Introduction", "introduction"))
    out.append(sec("Description", "description"))
    out.append(sec("Explanation", "explanation"))
    out.append(sec("Self Assessment", "selfAssesment"))
    out.append(sec("Additional Resources", "additionalResources"))
    # Trim extra blank lines while keeping structure.
    text = "\n".join([s for s in out if s is not None])
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def _fetch_and_process_topic(key: str, base_url: str, out_dir: str, fmt: str) -> Optional[Dict[str, Any]]:
    topic_url = f"{base_url}/current/concepts/{urllib.parse.quote(str(key))}.json"
    try:
        topic = _http_get_json(topic_url)
    except Exception as e:
        print(f"Failed to fetch topic {key}: {e}")
        return None

    if not isinstance(topic, dict):
        return None

    code = topic.get("code") or str(key)
    safe = _safe_filename(code)

    if fmt in ("json", "both"):
        _write_json(os.path.join(out_dir, f"{safe}.json"), topic)
    if fmt in ("md", "both"):
        _write_text(os.path.join(out_dir, f"{safe}.md"), _topic_to_markdown(topic))

    return {
        "key": key,
        "code": topic.get("code"),
        "name": topic.get("name"),
        "link": topic.get("link"),
        "out_base": os.path.join(out_dir, safe),
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Export UCGIS BoK topics (Firebase RTDB) to local files"
    )
    ap.add_argument("--base", default=DEFAULT_BASE, help="Firebase RTDB base URL")
    ap.add_argument(
        "--out",
        default=os.path.join("references", "ucgis-bok", "topics"),
        help="Output directory for exported topics",
    )
    ap.add_argument(
        "--format",
        choices=["json", "md", "both"],
        default="both",
        help="Output format",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of topics (0 = all)",
    )
    ap.add_argument(
        "--sleep",
        type=float,
        default=0.05,
        help="Sleep seconds between topic requests (ignored in concurrent mode)",
    )
    args = ap.parse_args()

    # 1) Discover current keys
    keys_url = f"{args.base}/current/concepts.json?shallow=true"
    keys_obj = _http_get_json(keys_url)
    if not isinstance(keys_obj, dict):
        raise RuntimeError(f"Unexpected response from {keys_url}")
    keys = sorted(keys_obj.keys(), key=lambda x: int(x) if str(x).isdigit() else str(x))
    if args.limit and args.limit > 0:
        keys = keys[: args.limit]

    manifest = {
        "source": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
        "api": {"base": args.base, "keys_url": keys_url},
        "exported_at": time.strftime("%Y-%m-%d"),
        "count": 0,
        "topics": [],
    }

    # 2) Fetch each topic
    # Using 10 workers as a reasonable default for I/O bound operations against a public API
    max_workers = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                _fetch_and_process_topic, key, args.base, args.out, args.format
            ): key
            for key in keys
        }

        completed_count = 0
        total = len(keys)

        for future in concurrent.futures.as_completed(futures):
            key = futures[future]
            try:
                result = future.result()
                if result:
                    manifest["topics"].append(result)
            except Exception as exc:
                print(f"Topic {key} generated an exception: {exc}")

            completed_count += 1
            if completed_count % 25 == 0:
                print(f"Fetched {completed_count}/{total}")

    # Sort topics to maintain deterministic output order
    manifest["topics"].sort(key=lambda t: int(t["key"]) if str(t["key"]).isdigit() else str(t["key"]))
    manifest["count"] = len(manifest["topics"])

    _write_json(os.path.join(args.out, "manifest.json"), manifest)
    print(f"Done. Exported {manifest['count']} topics to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
