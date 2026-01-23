import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
MANIFEST_PATH = ROOT / "references" / "ucgis-bok" / "topics" / "manifest.json"


FILE_BOK = {
    # Keyed by file stem (path without extension)
    "chapter-00-welcome": ["FC-01-038", "FC-04", "FC-06"],
    "chapter-01-spatial-data": [
        "DM-02-014",
        "DM-02-007",
        "CV-02-003",
        "CV-02-020",
        "DM-06-086",
        "FC-06",
    ],
    "chapter-02-map-design": ["CV-03", "CV-04", "CV-01-001", "CV-01-026", "CV-04-018"],
    "chapter-03-projections": [
        "CV-03-006",
        "DM-05-047",
        "DM-05-048",
        "DM-05-052",
        "DM-05-051",
    ],
    "chapter-04-gps": ["DC-02-003", "DC-06-009", "DM-05-052", "DM-05-047", "GS-01-004"],
    "chapter-05-georeferencing": ["DC-01-030", "DM-05", "DC-02-010", "DM-06-087", "DM-02-007"],
    "chapter-05-analysis": [
        "AM-01-020",
        "AM-02-003",
        "AM-02-004",
        "AM-02-006",
        "AM-05-076",
        "GS-02-025",
    ],
    "chapter-06-digitizing": [
        "DM-02-014",
        "CV-02-003",
        "DC-04-014",
        "DC-01-025",
        "DM-06-086",
        "DC-06-009",
    ],
    "chapter-06-output": ["CV-03", "CV-04", "CV-01-001", "CV-01-026", "CV-04-018", "CV-05-040"],
    "chapter-07-database-management": [
        "DM-01-001",
        "DM-01-004",
        "FC-06-012",
        "DM-01-062",
        "DM-01-070",
        "DM-07-060",
    ],
    "chapter-08-vgi-neogeography": ["DC-02-029", "GS-02-024", "GS-02-028", "DM-02-071", "GS-01-004"],
    "chapter-08-georeferencing": ["DC-01-030", "DM-05", "DC-02-010", "DM-06-087", "DM-02-007"],
    "chapter-09-spectral-analysis": ["DC-03-016", "DC-04-035", "DC-03-031", "DC-03-026", "FC-05-021"],
    "chapter-10-remote-sensing": ["DC-03-026", "DC-03-016", "FC-05-021", "DC-03", "DC-04-014"],
    "chapter-11-image-classification": [
        "AM-02-009",
        "DC-04-014",
        "DC-03-016",
        "AM-03-026",
        "DC-04-019",
        "AM-09-104",
    ],
    "chapter-12-lidar": ["DC-03-027", "AM-04-099", "AM-04-055", "AM-04-064", "DC-03-040"],
    "chapter-13-raster-analysis": [
        "DM-02-007",
        "DM-06-087",
        "AM-02-006",
        "FC-05-042",
        "AM-04-055",
        "AM-04-064",
    ],
    "chapter-14-vector-analysis": [
        "DM-02-014",
        "AM-02-003",
        "AM-02-004",
        "DM-04-077",
        "FC-05-042",
        "DM-06-086",
    ],
    "chapter-15-spatial-modeling": [
        "AM-01-020",
        "GS-02-025",
        "PD-02-025",
        "AM-09-107",
        "AM-09-106",
        "AM-03-019",
    ],
    "chapter-16-mobile-gis": ["CP-01-015", "DC-02-005", "CV-05-040", "DC-06-009", "GS-01-004"],
    "chapter-17-storytelling": ["CV-04-033", "CV-03", "CV-04", "CV-04-018", "CV-01-026"],
    "chapter-18-gis-ethics": ["GS-02-011", "GS-03-014", "GS-01-004", "GS-03-021", "GS-01-027", "CV-01-026"],
    "chapter-19-artificial-intelligence": [
        "AM-08-093",
        "AM-08-094",
        "AM-08-038",
        "CP-04-004",
        "AM-02-009",
        "DC-04-014",
    ],
    "chapter-20-research-data-management": [
        "DM-07-057",
        "DM-07-060",
        "GS-01-023",
        "PD-02-022",
        "PD-05-033",
        "AM-09-107",
    ],
    "chapter-21-research-in-gis": ["FC-06", "AM-03-019", "PD-02-025", "AM-09-107", "GS-02-011", "GS-02-025"],
    "chapter-22-lifelong-learning": ["KE-01-023", "KE-01-025", "KE-01-031", "GS-02-012"],
    "chapter-23-vgi": ["DC-02-029", "GS-02-024", "GS-02-028", "DM-02-071", "GS-01-004"],
}


def load_topics():
    manifest = json.loads(MANIFEST_PATH.read_text("utf-8"))
    by_code = {}
    for t in manifest.get("topics", []):
        code = t.get("code")
        if code:
            by_code[code] = t
    return by_code


def bok_section(chapter_code: str, topic_codes: list[str], by_code: dict) -> str:
    items = []
    for code in topic_codes:
        t = by_code.get(code)
        if not t:
            continue
        name = t.get("name") or code
        link = t.get("link") or "https://gistbok-ltb.ucgis.org/"
        items.append(
            """
        <li class="bok-topic">
            <span class="bok-code">{code}</span>
            <a href="{link}" target="_blank" rel="noopener noreferrer">{name}</a>
        </li>""".format(
                code=code, link=link, name=name
            ).strip("\n")
        )

    # Always include a platform link even if topic list is empty.
    extra = (
        """
        <li class="bok-topic">
            <span class="bok-code">BoK</span>
            <a href="https://gistbok-ltb.ucgis.org/" target="_blank" rel="noopener noreferrer">UCGIS GIS&T Body of Knowledge (Living Textbook)</a>
        </li>""".strip("\n")
    )
    if items:
        items.append(extra)
    else:
        items = [extra]

    return (
        """

        <section class="card bok-alignment" aria-label="Body of Knowledge alignment">
            <h2>BoK Alignment</h2>
            <p>
                Topics in the UCGIS GIS&amp;T Body of Knowledge that support this chapter.
            </p>
            <ul class="bok-topic-list">
{items}
            </ul>
        </section>
""".rstrip()
        .format(items="\n".join(["                " + x for x in items]))
    )


def chapter_key_from_filename(name: str) -> str | None:
    # Key is the file stem.
    if not name.endswith(".html"):
        return None
    return name[:-5]


def main() -> int:
    by_code = load_topics()
    paths = sorted(CHAPTERS_DIR.glob("chapter-*.html"))
    updated = 0
    skipped = 0

    for p in paths:
        html = p.read_text("utf-8", errors="ignore")
        if "bok-alignment" in html:
            skipped += 1
            continue

        key = chapter_key_from_filename(p.name)
        if not key:
            skipped += 1
            continue

        topic_codes = FILE_BOK.get(key)
        if topic_codes is None:
            skipped += 1
            continue

        block = bok_section(key, topic_codes, by_code)

        marker = "</main>"
        idx = html.rfind(marker)
        if idx == -1:
            skipped += 1
            continue

        out = html[:idx] + block + "\n\n" + html[idx:]
        p.write_text(out, "utf-8", newline="\n")
        updated += 1

    print(f"Updated: {updated}; Skipped: {skipped}; Total: {len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
