import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"


def _load_insert_module():
    path = ROOT / "scripts" / "insert_bok_alignment.py"
    spec = importlib.util.spec_from_file_location("insert_bok_alignment", path)
    if not spec or not spec.loader:
        raise RuntimeError("Unable to load insert_bok_alignment.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def replace_or_insert(html: str, block: str) -> str | None:
    start = html.find('<section class="card bok-alignment"')
    if start != -1:
        end = html.find("</section>", start)
        if end == -1:
            return None
        end += len("</section>")
        return html[:start] + block + html[end:]

    idx = html.rfind("</main>")
    if idx == -1:
        return None
    return html[:idx] + block + "\n\n" + html[idx:]


def main() -> int:
    insert_mod = _load_insert_module()
    file_bok = insert_mod.FILE_BOK
    bok_section = insert_mod.bok_section
    by_code = insert_mod.load_topics()
    paths = sorted(CHAPTERS_DIR.glob("chapter-*.html"))
    updated = 0
    skipped = 0

    for p in paths:
        key = p.stem
        topic_codes = file_bok.get(key)
        if topic_codes is None:
            skipped += 1
            continue

        block = bok_section(key, topic_codes, by_code)
        html = p.read_text("utf-8", errors="ignore")
        out = replace_or_insert(html, block)
        if not out:
            skipped += 1
            continue
        p.write_text(out, "utf-8", newline="\n")
        updated += 1

    print(f"Updated: {updated}; Skipped: {skipped}; Total: {len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
