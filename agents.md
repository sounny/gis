# AGENTS.MD: The "Gold Standard" Protocol

**Status:** Active Strategy
**Last Updated:** January 23, 2026
**Visionary:** Dr. Sounny
**Architect:** Conductor / Gemini

---

## 1. The Core Philosophy: "GIS is an Art"

To make this the "best GIS book ever," we must move beyond the dry, technical manual format of standard textbooks. We adopt Dr. Sounny's perspective: **GIS is an Art.**

- **The Medium:** The textbook is not just a reference; it is an _experience_. It must be as visually compelling as the maps we teach students to create.
- **The Narrative:** Data alone is boring. We use **Storytelling** (Scrollytelling, Case Studies) to weave technical concepts into human narratives.
- **The Lens:** We view the world through **Remote Sensing** and **Spatial Thinking**, not just button-clicking.

## 2. The "Gold Standard" Feature Set

Every chapter must contain these non-negotiable pedagogical components to ensure depth and engagement:

### A. The "Local to Global" Connection

- **Why:** Students learn best when they connect abstract global concepts to tangible local realities.
- **Implementation:** Every chapter features a **Sidebar** connecting the topic (e.g., Sea Level Rise) to a specific **Texas context** (e.g., Galveston subsidence) and then linking it back to a global parallel (e.g., Venice).

### B. Interactive "Simulators" over "Screenshots"

- **Why:** Passive reading is passive learning. GIS is a kinetic skill.
- **Implementation:**
  - **Do not** just show a static image of a histogram; build an **interactive slider** (see Ch 09).
  - **Do not** just explain GPS trilateration; build a **canvas-based simulator** where students drag satellites (see Ch 04).
  - **Do not** just list SQL commands; provide a **sandbox** (see Ch 07).
- **Tech Stack:** Pure Vanilla JS + Canvas API. No heavy frameworks. Keep it lightweight, fast, and hackable.

### C. Humanizing the Science ("Important Persons")

- **Why:** Science is a human endeavor. Students need to see the diverse faces behind the algorithms.
- **Implementation:** "Bio Boxes" highlighting pioneers like **Gladys West** (GPS), **Virginia Norwood** (Landsat), and **Dana Tomlin** (Map Algebra).

### D. Critical GIS & Ethics

- **Why:** Maps are power. A "best" book must teach responsibility.
- **Implementation:** We do not shy away from "Bad Maps," Gerrymandering, or Privacy issues. We use tools like the **Ethics Simulator** (Ch 18) to force students to make difficult choices.

## 3. The Lab Manual Protocol (Tri-Platform)

We are building a robust Lab Manual that supports **ArcGIS Pro**, **QGIS**, and **Web GIS** simultaneously.

- **Architecture:** Labs use a **Tabbed Interface** (`labs/_template.html`).
- **Usage:**
  1.  **Duplicate** `labs/_template.html` to create a new lab (e.g., `labs/lab-99-new-topic.html`).
  2.  **Scenario:** Write ONE universal scenario and data download section.
  3.  **Instructions:** Fill in the `<div class="instruction-pane">` for each platform (ArcGIS, QGIS, Web).
  4.  **JavaScript:** The switching logic is handled automatically by `labs/js/lab-switcher.js`.
- **Status:** The infrastructure is ready (`labs/index.html`, `labs/css/lab.css`). Placeholder files exist, but the _content_ for each lab needs to be written by a subject matter expert.

## 4. Technical Architecture for Longevity

To ensure this book survives software version cycles:

- **Static First:** Pure HTML/CSS/JS. No build steps, no databases, no fragile dependencies. It runs on a potato.
- **Semantic Structure:** `index.html` is the source of truth. Folder structures are flat and predictable (`chapters/`, `assets/`, `css/`).
- **Accessibility:** High contrast, responsive design (verified on mobile), and semantic HTML for screen readers.

## 5. Future Directive for Agents

If you are an agent reading this to improve the book, follow this decision matrix:

1.  **Is it Interactive?** If you are writing a paragraph explaining a process, stop. Can you build a JS tool to _show_ it instead?
2.  **Is it Local?** Have you connected this concept to Texas? If not, search the `references/` folder for a local case study.
3.  **Is it Beautiful?** Does the CSS pop? Are we using the "Premium, Minimalist, Modern" aesthetic defined in `style.css`?
4.  **Is it Connected?** Ensure navigation flows logically. Chapter 09 connects to 09b, which connects to 10. The user journey is continuous.

---

## 6. OCNOTES (Reference Mining Output)

When you see files named `*.html.OCNOTES.md`, they are **proposed insertions** mined from `references/`.

- **Purpose:** Give future agents a fast map from each book page \u2192 key concepts \u2192 supporting source material in `references/` (with excerpt seeds).
- **Protocol:** Do not edit the chapter/lab HTML directly from OCNOTES. Instead, adapt/paraphrase the OCNOTES material into the actual page in a focused follow-up PR/commit.
- **Generator:** `scripts/generate_ocnotes.py` regenerates OCNOTES for `index.html`, `chapters/*.html`, and `labs/*.html`.

---

**"We are in the Digital Age of Exploration... go out and discover something new!"**

---

## 7. Known Issues / To Do

- **Action Item (Claude):** The visual alignment of the "GIS Hero" sidebar in Chapter 00 works functionally but does not perfectly match the "Local to Global" sidebar's aesthetic polish. This needs to be revisited and solved (likely by Claude) to ensure pixel-perfect consistency across all sidebar types.
