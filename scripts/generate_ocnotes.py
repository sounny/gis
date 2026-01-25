"""Generate *.OCNOTES.md files for book pages.

Goal:
- For each HTML page in the book (root index, chapters/*.html, labs/*.html),
  extract visible concepts (key terms, glossary terms, headings).
- For each concept, search text-like materials under references/ to surface
  candidate sources and excerpt seeds.
- Write a peer-agent-friendly markdown file next to each page with the same
  name plus `.OCNOTES.md`.

This script does NOT modify the actual book pages.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
REF_ROOT = ROOT / "references"

PAGE_DIRS = [ROOT, ROOT / "chapters", ROOT / "labs"]
PAGE_GLOBS = ["index.html", "*.html"]

REF_EXTS = {".md", ".txt", ".html", ".htm"}
MAX_REF_CHARS = 250_000

TAG_RE = re.compile(r"<[^>]+>")

STOP_EXACT = {
    "At a Glance",
    "Learning outcomes",
    "Key terms",
    "Stop & check",
    "Stop &amp; check",
    "Try it (5 minutes)",
    "Lab (Two Tracks)",
    "Common mistakes",
    "Summary of Big Ideas",
    "BoK Alignment",
    "Chapter Glossary",
    "Checkpoint",
    "Lab",
    "Scenario",
    "Deliverable",
}

STOP_SUBSTR = {
    "Back to Dashboard",
    "Texas Connection",
    "BoK Alignment",
    "Stop & check",
    "Try it",
    "Common mistakes",
    "Checkpoint",
}

STOP_PATTERNS = [
    re.compile(r"^Chapter\s+\d+\b", re.I),
    re.compile(r"^Lab\s+\d+\b", re.I),
]


SIM_IDEAS: list[tuple[list[str], str]] = [
    (
        ["spatial data", "vector", "raster", "topology"],
        "Model picker: give 6 real questions (pipes, flood surface, landcover, parcels, temperature, crime points) and have students choose vector/raster + why; reveal tradeoffs (file size, topology, mixed pixels).",
    ),
    (
        ["map design", "cartography", "symbol", "color", "classification", "legend", "typography"],
        "Legend lab: interactive map where students change classification (quantiles/jenks/equal interval) and see how the story changes; include a 'bad map' toggle.",
    ),
    (
        ["projection", "projections", "mercator", "utm", "datum"],
        "Projection distortion viewer: canvas globe with selectable projection; show Tissot indicatrices + area/shape distortion; compare Texas vs global.",
    ),
    (
        ["gps", "gnss", "trilateration", "satellite"],
        "Trilateration simulator: drag satellites, watch intersection/error ellipse change; add 'urban canyon' multipath toggle.",
    ),
    (
        ["georeferencing", "control point", "gcp", "rubbersheet"],
        "Georeferencing game: drag GCPs onto matching features; live RMS error readout; show how bad points warp the map.",
    ),
    (
        ["database", "sql", "query", "postgres", "postgis", "normalization"],
        "SQL sandbox: small in-browser table + query runner; include joins and a simple 'spatial join' (within distance) visual.",
    ),
    (
        ["remote sensing", "electromagnetic", "spectral"],
        "Spectral slider: move wavelength slider across EM spectrum and reveal what sensors 'see'; pair with a Texas target (Houston heat, coastal water, agriculture).",
    ),
    (
        ["spectral analysis", "ndvi", "indices", "histogram"],
        "Index builder: compute NDVI/NDWI on a tiny raster; histogram + threshold slider; show false-color composites.",
    ),
    (
        ["classification", "supervised", "unsupervised", "accuracy assessment", "confusion matrix"],
        "Classifier simulator: pick training points on a tiny image, run a toy classifier, then compute confusion matrix + overall/producer/user accuracy.",
    ),
    (
        ["lidar", "point cloud", "dem"],
        "Point-cloud slicer: show a synthetic point cloud, let students move a cross-section plane; derive DEM/CHM; discuss density + occlusion.",
    ),
    (
        ["raster analysis", "map algebra", "suitability", "cost distance"],
        "Suitability studio: weighted overlay sliders; show how weights change the final 'best site'; include an ethics prompt about who benefits.",
    ),
    (
        ["vector analysis", "buffer", "overlay", "intersect", "union", "network"],
        "Vector overlay playground: buffer distance slider, live area/feature count updates; show dissolve vs no-dissolve.",
    ),
    (
        ["storytelling", "scrollytelling", "narrative"],
        "Scrollytelling template: 4 panels + map state transitions; students swap in their own Texas case study.",
    ),
    (
        ["ethics", "privacy", "bias", "surveillance"],
        "Ethics simulator extension: choose data resolution/aggregation, see privacy risk vs utility score; require a written justification.",
    ),
    (
        ["vgi", "crowdsourcing", "openstreetmap"],
        "VGI reliability meter: show edits from multiple contributors, let students accept/reject with confidence; compute completeness + bias metrics.",
    ),
    (
        ["mobile", "field", "collector"],
        "Field data form builder: preview form + validation; simulate GNSS accuracy, photo attachments, and offline sync conflict.",
    ),
    (
        ["artificial intelligence", "machine learning", "ai"],
        "AI map critique: show model output heatmap + threshold slider; students label failure modes (bias, overfit, spurious correlation).",
    ),
    (
        ["research", "research data management", "metadata", "doi", "reproducible"],
        "Reproducibility checklist widget: interactive checklist that generates a 'methods + data' appendix skeleton.",
    ),
]


@dataclass(frozen=True)
class RefHit:
    count: int
    path: str
    excerpt: str


def _clean_text(raw: str) -> str:
    txt = TAG_RE.sub("", raw)
    txt = txt.replace("\xa0", " ").replace("📚", " ")
    txt = re.sub(r"\s+", " ", txt)
    return txt.strip()


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return _clean_text(m.group(1)) if m else ""


def extract_concepts(html: str) -> list[str]:
    concepts: list[str] = []

    # Key terms scaffold
    km = re.search(r"<h3>\s*Key terms\s*</h3>\s*<p>(.*?)</p>", html, re.I | re.S)
    if km:
        kt = _clean_text(km.group(1))
        for part in kt.split(","):
            term = part.strip()
            if term:
                concepts.append(term)

    # Glossary terms
    for m in re.finditer(r"<span class=\"glossary-term\">\s*(.*?)\s*</span>", html, re.I | re.S):
        term = _clean_text(m.group(1))
        if term:
            concepts.append(term)

    # Headings
    for m in re.finditer(r"<h[1-3][^>]*>(.*?)</h[1-3]>", html, re.I | re.S):
        t = _clean_text(m.group(1))
        if not t:
            continue
        if t in STOP_EXACT:
            continue
        if any(s.lower() in t.lower() for s in STOP_SUBSTR):
            continue
        if any(p.search(t) for p in STOP_PATTERNS):
            continue
        concepts.append(t)

    # Dedup + filter trivial
    out: list[str] = []
    seen: set[str] = set()
    for t in concepts:
        if len(t) < 4:
            continue
        tl = t.lower()
        if tl in {"gis", "map", "data", "analysis", "introduction", "overview", "summary", "system"}:
            continue
        if t not in seen:
            seen.add(t)
            out.append(t)
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


def find_refs(ref_texts: dict[str, str], term: str, max_hits: int = 3) -> list[RefHit]:
    tl = term.lower().strip()
    if len(tl) < 4:
        return []
    if tl in {"gis", "map", "data", "analysis", "model", "models", "system", "chapter", "lab"}:
        return []

    scores: list[tuple[int, str, str]] = []
    for path, txt in ref_texts.items():
        cnt = txt.lower().count(tl)
        if cnt:
            scores.append((cnt, path, txt))
    scores.sort(reverse=True, key=lambda x: x[0])

    hits: list[RefHit] = []
    for cnt, path, txt in scores[:max_hits]:
        idx = txt.lower().find(tl)
        excerpt = ""
        if idx != -1:
            start = max(0, idx - 200)
            end = min(len(txt), idx + 320)
            excerpt = re.sub(r"\s+", " ", txt[start:end].replace("\n", " ")).strip()
        hits.append(RefHit(count=cnt, path=path, excerpt=excerpt))
    return hits


def best_overall_sources(ref_texts: dict[str, str], concepts: Iterable[str], cap: int = 12) -> list[tuple[str, int]]:
    tally: dict[str, int] = {}
    for c in concepts:
        for h in find_refs(ref_texts, c, max_hits=6):
            tally[h.path] = tally.get(h.path, 0) + h.count
    return sorted(tally.items(), key=lambda x: x[1], reverse=True)[:cap]


def pick_sim_ideas(concepts: list[str]) -> list[str]:
    blob = " ".join(c.lower() for c in concepts)
    ideas: list[str] = []
    for keys, idea in SIM_IDEAS:
        if any(k in blob for k in keys):
            ideas.append(idea)
    # Dedup preserve order
    out: list[str] = []
    seen: set[str] = set()
    for i in ideas:
        if i not in seen:
            seen.add(i)
            out.append(i)
    return out[:4]


def iter_pages() -> list[Path]:
    pages: list[Path] = []
    # root index only
    if (ROOT / "index.html").exists():
        pages.append(ROOT / "index.html")

    for d in (ROOT / "chapters", ROOT / "labs"):
        if not d.exists():
            continue
        pages.extend(sorted([p for p in d.glob("*.html") if p.is_file()]))

    # Chapter shared components (book infrastructure)
    comp_dir = ROOT / "chapters" / "_components"
    if comp_dir.exists():
        pages.extend(sorted([p for p in comp_dir.glob("*.html") if p.is_file()]))

    return pages


def write_notes(ref_texts: dict[str, str], page: Path) -> None:
    html = page.read_text(encoding="utf-8", errors="ignore")
    title = extract_title(html)
    concepts = extract_concepts(html)
    sources = best_overall_sources(ref_texts, concepts)
    sim_ideas = pick_sim_ideas(concepts + ([title] if title else []))

    candidate_excerpts: list[tuple[str, str]] = []
    for path, _score in sources[:6]:
        txt = ref_texts.get(path, "").strip()
        if not txt:
            continue
        snippet = re.sub(r"\s+", " ", txt)[:420]
        candidate_excerpts.append((path, snippet))
        if len(candidate_excerpts) >= 4:
            break

    lines: list[str] = []
    lines.append(f"# OCNOTES: {page.name}")
    if title:
        lines.append("")
        lines.append(f"Page title: {title}")
    lines.append("")
    lines.append(f"Source page: `{page.as_posix()}`")

    lines.append("")
    lines.append("## Concepts found on page")
    if concepts:
        for c in concepts[:50]:
            lines.append(f"- {c}")
        if len(concepts) > 50:
            lines.append(f"- (truncated) total concepts detected: {len(concepts)}")
    else:
        lines.append("- (No concepts auto-detected; consider adding key terms/headings.)")

    lines.append("")
    lines.append("## Strongest reference sources (overall)")
    if sources:
        for path, score in sources:
            lines.append(f"- `{path}` (signal={score})")
    else:
        lines.append("- (No matching reference sources found by simple term search.)")

    lines.append("")
    lines.append("## Candidate excerpts to adapt (verbatim seeds; paraphrase into the chapter)")
    if candidate_excerpts:
        for path, ex in candidate_excerpts:
            lines.append(f"- `{path}`")
            lines.append(f"  {ex}...")
    else:
        lines.append("- (None automatically selected.)")

    lines.append("")
    lines.append("## Reference matches by concept (top hits)")
    any_hits = False
    for c in concepts[:30]:
        hits = find_refs(ref_texts, c, max_hits=2)
        if not hits:
            continue
        any_hits = True
        lines.append("")
        lines.append(f"### {c}")
        for h in hits:
            ex = (h.excerpt[:260] + "...") if len(h.excerpt) > 260 else h.excerpt
            lines.append(f"- `{h.path}` (matches={h.count})")
            if ex:
                lines.append(f"  Excerpt: {ex}")
    if not any_hits:
        lines.append("")
        lines.append("- (No per-concept hits found; consider searching references by synonyms.)")

    lines.append("")
    lines.append("## Proposed adaptation to the book (concrete next edits for another agent)")
    if sim_ideas:
        lines.append("- Interactive module candidates:")
        for idea in sim_ideas:
            lines.append(f"  - {idea}")
    else:
        lines.append("- Interactive module candidates: (none auto-suggested; see AGENTS.md decision matrix)")

    lines.append(
        "- Local-to-Global sidebar: search within the listed reference sources for a Texas anchor (Houston, Galveston, Austin, DFW, Rio Grande, Permian Basin) and write a 120-180 word sidebar that ends with a global parallel."
    )
    lines.append(
        "- 'Important Persons' bio box: if any reference source includes an inventor/author tied to this topic, add a 1-paragraph bio + 3 bullets (impact, algorithm/idea, modern use)."
    )
    lines.append(
        "- Critical GIS prompt: add 1 dilemma question connected to the chapter's primary dataset choice (scale, privacy, bias, uncertainty) and ask for a written justification."
    )

    out_path = page.with_suffix(page.suffix + ".OCNOTES.md")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    pages = iter_pages()
    print(f"Found {len(pages)} pages")
    ref_texts = load_reference_texts()
    print(f"Loaded {len(ref_texts)} reference text files")

    for i, page in enumerate(pages, 1):
        write_notes(ref_texts, page)
        if i % 7 == 0 or i == len(pages):
            print(f"Wrote {i}/{len(pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
