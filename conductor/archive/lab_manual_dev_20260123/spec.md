# Specification: Lab Manual Development (Tri-Platform Strategy)

## Goal
To develop a comprehensive "Lab Manual" for the GIS Digital Textbook where every lab exercises the same learning outcomes across three distinct platforms: **ArcGIS Pro** (Desktop/Proprietary), **QGIS** (Desktop/Open Source), and **Web GIS** (Cloud/Browser-based).

## Strategic Architecture: The "Tri-Platform" Lab
Each Lab will be a standalone HTML page (e.g., `labs/lab-01-spatial-data.html`) featuring:
1.  **Unified Scenario:** A real-world problem statement (e.g., "Map the flood risk in Austin") that applies to all users.
2.  **Universal Data:** A single data package (ZIP) containing formats readable by all three platforms (e.g., Shapefile, GeoJSON, GeoTIFF).
3.  **Tabbed Instruction Interface:** A custom HTML/JS component allowing the user to toggle the "Step-by-Step" section between:
    - 🟦 **ArcGIS Pro**
    - 🟩 **QGIS**
    - 🟧 **Web GIS**
4.  **Common Deliverable:** A unified assessment criteria (e.g., "Export a map PDF with these 5 elements").

## Scope
- **Architecture:** Create `css/lab-style.css` and `js/lab-tabs.js` to handle the switching logic.
- **Content:** Develop 10-12 Core Labs covering the major textbook parts.
- **Integration:** Create a dedicated "Lab Manual" index section on the homepage.

## Lab Curriculum (Proposed)
*   **Lab 01 (Data):** The Vector vs. Raster Safari (Data exploration).
*   **Lab 02 (Design):** Choropleth Mapping (Symbolization).
*   **Lab 03 (Projections):** The Distortion Challenge (Re-projecting data).
*   **Lab 04 (GPS):** Phone-to-Map Workflow (CSV import).
*   **Lab 05 (Georeferencing):** Warping History (Georeferencing an old map).
*   **Lab 06 (Digitizing):** Creating New Data (Tracing features).
*   **Lab 07 (RS):** False Color Detective (Band combinations).
*   **Lab 08 (Analysis):** Site Selection (Buffer/Intersect overlay).
*   **Lab 09 (Mobile):** Field Data Design (Survey form creation).
*   **Lab 10 (Story):** Narrative Mapping (StoryMap/Web App builder).

## Technical Requirements
- **Responsive:** Labs must be readable on tablets (for second-screen use while working on desktop).
- **Self-Contained:** Labs should link directly to their specific data downloads.
- **Consistent Styling:** Use the existing "Premium/Modern" aesthetic.

## Assessment Criteria
- A generic "Lab Report Template" (Markdown/Word) provided for students.
- Labs must be testable: "Did the student produce the correct map?"
