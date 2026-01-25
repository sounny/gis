"""Generate per-chapter sidebar draft notes: *.OCSIDEBARs.md

For each chapter HTML page in chapters/*.html, emit a markdown companion file
next to it with three sidebar draft blocks:

- GIS Is an Art
- Asking Questions of Where
- Interdisciplinary Thinking

Each sidebar includes:
- a draft (agent-editable) paragraph
- a few prompts/activity ideas
- reference seeds (file paths + short excerpts) from references/

This script does NOT modify any chapter HTML.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
REF_ROOT = ROOT / "references"

REF_EXTS = {".md", ".txt", ".html", ".htm"}
MAX_REF_CHARS = 250_000

TAG_RE = re.compile(r"<[^>]+>")

TEXAS_TERMS = [
    "texas",
    "austin",
    "houston",
    "dallas",
    "fort worth",
    "san antonio",
    "el paso",
    "galveston",
    "travis",
    "harris",
    "rio grande",
    "gulf",
    "permian",
]


@dataclass(frozen=True)
class RefHit:
    path: str
    score: int
    excerpt: str


def clean_text(raw: str) -> str:
    txt = TAG_RE.sub("", raw)
    txt = txt.replace("\xa0", " ")
    txt = re.sub(r"\s+", " ", txt)
    return to_ascii(txt).strip()


def to_ascii(s: str) -> str:
    """Best-effort ASCII normalization for notes files.

    We keep the notes readable in plain terminals and avoid introducing
    non-ASCII unless the source already requires it.
    """

    return "".join(ch for ch in s if ord(ch) < 128)


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return clean_text(m.group(1)) if m else ""


def extract_concepts(html: str) -> list[str]:
    concepts: list[str] = []

    # Key terms scaffold
    km = re.search(r"<h3>\s*Key terms\s*</h3>\s*<p>(.*?)</p>", html, re.I | re.S)
    if km:
        kt = clean_text(km.group(1))
        for part in kt.split(","):
            term = part.strip()
            if term:
                concepts.append(term)

    # H2/H3 headings
    for m in re.finditer(r"<h[23][^>]*>(.*?)</h[23]>", html, re.I | re.S):
        h = clean_text(m.group(1))
        if not h:
            continue
        # Filter obvious UI headings
        if h.lower() in {
            "at a glance",
            "learning outcomes",
            "key terms",
            "stop & check",
            "try it (5 minutes)",
            "lab (two tracks)",
            "common mistakes",
            "summary of big ideas",
            "bok alignment",
            "chapter glossary",
            "checkpoint",
        }:
            continue
        concepts.append(h)

    # Dedup
    out: list[str] = []
    seen: set[str] = set()
    for c in concepts:
        c = c.strip()
        if len(c) < 4:
            continue
        if c.lower() in {"gis", "map", "data", "analysis", "introduction", "overview", "summary"}:
            continue
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def load_reference_texts() -> dict[str, str]:
    texts: dict[str, str] = {}
    for p in REF_ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in REF_EXTS:
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if len(txt) > MAX_REF_CHARS:
            txt = txt[:MAX_REF_CHARS]
        texts[p.as_posix()] = txt
    return texts


def find_best_sources(ref_texts: dict[str, str], concepts: list[str], cap: int = 12) -> list[tuple[str, int]]:
    tally: dict[str, int] = {}
    for concept in concepts:
        key = concept.lower()
        if len(key) < 4:
            continue
        if key in {"gis", "map", "data", "analysis", "model", "models", "system", "chapter"}:
            continue
        for path, txt in ref_texts.items():
            cnt = txt.lower().count(key)
            if cnt:
                tally[path] = tally.get(path, 0) + cnt
    return sorted(tally.items(), key=lambda x: x[1], reverse=True)[:cap]


def excerpt_around(txt: str, needle: str, window: int = 220) -> str:
    low = txt.lower()
    n = needle.lower()
    idx = low.find(n)
    if idx == -1:
        return ""
    start = max(0, idx - window)
    end = min(len(txt), idx + window)
    ex = txt[start:end].replace("\n", " ")
    ex = re.sub(r"\s+", " ", ex).strip()
    return to_ascii(ex)


def texas_hits(
    ref_texts: dict[str, str],
    prefer_paths: list[str],
    concepts: list[str],
    cap: int = 4,
) -> list[RefHit]:
    """Find Texas-relevant reference seeds.

    Strategy:
    1) Prefer chapter-relevant sources (prefer_paths).
    2) If none are found, broaden to the full corpus but require both:
       - a Texas term, and
       - at least one strong chapter concept keyword.
    """

    def scan_paths(paths: list[str]) -> list[RefHit]:
        out: list[RefHit] = []
        for path in paths:
            txt = ref_texts.get(path, "")
            if not txt:
                continue
            score = 0
            best_ex = ""
            for t in TEXAS_TERMS:
                cnt = txt.lower().count(t)
                if cnt:
                    score += cnt
                    if not best_ex:
                        best_ex = excerpt_around(txt, t)
            if score:
                out.append(RefHit(path=path, score=score, excerpt=best_ex))
        out.sort(key=lambda h: h.score, reverse=True)
        return out

    hits = scan_paths(prefer_paths)
    if hits:
        return hits[:cap]

    # Broaden: Texas + chapter concepts
    concept_keys = [c.lower() for c in concepts if len(c) >= 5][:8]
    broad: list[RefHit] = []
    for path, txt in ref_texts.items():
        low = txt.lower()
        texas_score = sum(low.count(t) for t in TEXAS_TERMS)
        if not texas_score:
            continue
        concept_score = sum(low.count(k) for k in concept_keys)
        if not concept_score:
            continue
        # Use the first texas term that appears for excerpt
        ex = ""
        for t in TEXAS_TERMS:
            if t in low:
                ex = excerpt_around(txt, t)
                break
        broad.append(RefHit(path=path, score=texas_score + concept_score, excerpt=ex))
    broad.sort(key=lambda h: h.score, reverse=True)
    return broad[:cap]


def generic_hits(
    ref_texts: dict[str, str],
    queries: list[str],
    cap: int = 4,
    restrict_paths: list[str] | None = None,
) -> list[RefHit]:
    scored: dict[str, int] = {}
    excerpt_by_path: dict[str, str] = {}
    pool = restrict_paths if restrict_paths is not None else list(ref_texts.keys())
    for q in queries:
        ql = q.lower()
        for path in pool:
            txt = ref_texts.get(path, "")
            if not txt:
                continue
            cnt = txt.lower().count(ql)
            if not cnt:
                continue
            scored[path] = scored.get(path, 0) + cnt
            if path not in excerpt_by_path:
                excerpt_by_path[path] = excerpt_around(txt, q)
    hits = [RefHit(path=p, score=s, excerpt=excerpt_by_path.get(p, "")) for p, s in scored.items()]
    hits.sort(key=lambda h: h.score, reverse=True)
    return hits[:cap]


def slug_topic(chapter_file: Path, title: str) -> str:
    # Use filename stem as stable topic hint
    stem = chapter_file.stem
    stem = stem.replace("chapter-", "").replace("-", " ")
    if title:
        # Prefer the piece before "|" if present
        t = title.split("|")[0].strip()
        return f"{t} ({stem})"
    return stem


def sidebar_gis_art(topic: str) -> tuple[str, list[str]]:
    draft = (
        "GIS is an art because it turns messy reality into a deliberate visual argument. "
        "Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, "
        "reveals pattern, and makes a claim about what matters. "
        f"In this chapter on {topic}, treat the workflow like studio practice: iterate, compare alternatives, "
        "and explain your design choices (not just the button clicks)."
    )
    prompts = [
        "Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.",
        "Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?",
        "Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).",
    ]
    return draft, prompts


def sidebar_questions_of_where(topic: str) -> tuple[str, list[str]]:
    draft = (
        "Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: "
        "near/far, inside/outside, connected/disconnected, changing/stable. "
        f"For {topic}, the best work comes from translating a curiosity into a spatial test you can run and explain."
    )
    prompts = [
        "Where is it concentrated, and compared to what baseline?",
        "Where does it change sharply (boundaries) vs gradually (surfaces)?",
        "Where is the data missing, biased, or uncertain?",
        "Where would you stand on the ground to verify it (a field check plan)?",
    ]
    return draft, prompts


def sidebar_interdisciplinary(topic: str) -> tuple[str, list[str]]:
    draft = (
        "GIS becomes powerful when it borrows methods and questions from other fields. "
        "A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, "
        "environmental processes, and technology. "
        f"Use {topic} as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map."
    )
    prompts = [
        "Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?",
        "Urban planning: what zoning/transport constraint changes the interpretation of your result?",
        "Ecology/climate: what seasonal or physical process could explain the pattern?",
        "Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?",
    ]
    return draft, prompts


def write_sidebar_file(
    chapter_path: Path,
    title: str,
    concepts: list[str],
    top_sources: list[tuple[str, int]],
    art_refs: list[RefHit],
    where_refs: list[RefHit],
    inter_refs: list[RefHit],
    texas_refs: list[RefHit],
) -> None:
    topic = slug_topic(chapter_path, title)
    art_text, art_prompts = sidebar_gis_art(topic)
    where_text, where_prompts = sidebar_questions_of_where(topic)
    inter_text, inter_prompts = sidebar_interdisciplinary(topic)

    lines: list[str] = []
    lines.append(f"# OCSIDEBARs: {chapter_path.name}")
    if title:
        lines.append("")
        lines.append(f"Page title: {title}")
    lines.append("")
    lines.append(f"Source page: `{chapter_path.as_posix()}`")

    lines.append("")
    lines.append("## Concepts (for context)")
    for c in concepts[:30]:
        lines.append(f"- {c}")
    if len(concepts) > 30:
        lines.append(f"- (truncated) total concepts detected: {len(concepts)}")

    lines.append("")
    lines.append("## Sidebar: GIS Is an Art")
    lines.append("")
    lines.append(art_text)
    lines.append("")
    lines.append("Prompts:")
    for p in art_prompts:
        lines.append(f"- {p}")

    lines.append("")
    lines.append("Reference seeds:")
    if art_refs:
        for h in art_refs:
            ex = (h.excerpt[:260] + "...") if len(h.excerpt) > 260 else h.excerpt
            lines.append(f"- `{h.path}` (signal={h.score})")
            if ex:
                lines.append(f"  {ex}")
    else:
        lines.append("- (No strong matches found; consider MapDesign/Cartography references.)")

    lines.append("")
    lines.append("## Sidebar: Asking Questions of Where")
    lines.append("")
    lines.append(where_text)
    lines.append("")
    lines.append("Prompts:")
    for p in where_prompts:
        lines.append(f"- {p}")

    lines.append("")
    lines.append("Reference seeds:")
    if where_refs:
        for h in where_refs:
            ex = (h.excerpt[:260] + "...") if len(h.excerpt) > 260 else h.excerpt
            lines.append(f"- `{h.path}` (signal={h.score})")
            if ex:
                lines.append(f"  {ex}")
    else:
        lines.append("- (No strong matches found; consider Intro/SpatialThinking references.)")

    lines.append("")
    lines.append("## Sidebar: Interdisciplinary Thinking")
    lines.append("")
    lines.append(inter_text)
    lines.append("")
    lines.append("Prompts:")
    for p in inter_prompts:
        lines.append(f"- {p}")

    lines.append("")
    lines.append("Reference seeds:")
    if inter_refs:
        for h in inter_refs:
            ex = (h.excerpt[:260] + "...") if len(h.excerpt) > 260 else h.excerpt
            lines.append(f"- `{h.path}` (signal={h.score})")
            if ex:
                lines.append(f"  {ex}")
    else:
        lines.append("- (No strong matches found; consider DisasterMaps/econoGIS/BioGIS references.)")

    lines.append("")
    lines.append("## Texas anchor candidates (Local to Global fuel)")
    if texas_refs:
        for h in texas_refs:
            ex = (h.excerpt[:260] + "...") if len(h.excerpt) > 260 else h.excerpt
            lines.append(f"- `{h.path}` (texas_signal={h.score})")
            if ex:
                lines.append(f"  {ex}")
    else:
        lines.append("- (No Texas mentions found in the top-matching sources for this chapter.)")

    lines.append("")
    lines.append("## Top supporting sources (overall signal)")
    for path, score in top_sources[:12]:
        lines.append(f"- `{path}` (signal={score})")

    out_path = chapter_path.with_suffix(chapter_path.suffix + ".OCSIDEBARs.md")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    chapters = sorted([p for p in CHAPTERS_DIR.glob("chapter-*.html") if p.is_file()])
    print(f"Found {len(chapters)} chapter pages")
    ref_texts = load_reference_texts()
    print(f"Loaded {len(ref_texts)} reference text files")

    for i, ch in enumerate(chapters, 1):
        html = ch.read_text(encoding="utf-8", errors="ignore")
        title = extract_title(html)
        concepts = extract_concepts(html)
        top = find_best_sources(ref_texts, concepts)
        prefer_paths = [p for p, _s in top]

        texas = texas_hits(ref_texts, prefer_paths=prefer_paths, concepts=concepts, cap=4)

        # Prefer chapter-matching sources to keep seeds course-relevant.
        art_refs = generic_hits(
            ref_texts,
            ["cartography", "map design", "visual hierarchy", "symbol", "aesthetic"],
            cap=4,
            restrict_paths=prefer_paths,
        )
        if not art_refs:
            art_refs = generic_hits(ref_texts, ["cartography", "map design", "visual hierarchy", "symbol", "aesthetic"], cap=4)

        where_refs = generic_hits(
            ref_texts,
            ["spatial", "where", "pattern", "distribution"],
            cap=4,
            restrict_paths=prefer_paths,
        )
        if not where_refs:
            where_refs = generic_hits(ref_texts, ["spatial", "where", "pattern", "distribution"], cap=4)

        inter_refs = generic_hits(
            ref_texts,
            ["public health", "urban planning", "ecology", "climate", "econom", "disaster", "emergency", "transport"],
            cap=4,
            restrict_paths=prefer_paths,
        )
        if not inter_refs:
            inter_refs = generic_hits(
                ref_texts,
                ["public health", "urban planning", "ecology", "climate", "econom", "disaster", "emergency", "transport"],
                cap=4,
            )

        write_sidebar_file(
            chapter_path=ch,
            title=title,
            concepts=concepts,
            top_sources=top,
            art_refs=art_refs,
            where_refs=where_refs,
            inter_refs=inter_refs,
            texas_refs=texas,
        )

        if i % 6 == 0 or i == len(chapters):
            print(f"Wrote {i}/{len(chapters)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
