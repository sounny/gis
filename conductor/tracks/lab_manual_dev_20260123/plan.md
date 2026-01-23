# Implementation Plan: Lab Manual Development

## Phase 1: Architecture & Templates [checkpoint: a3df5c4]
- [x] **Task: Design Lab Layout** <!-- 5e31bd0 -->
    - [x] Create `labs/css/lab.css` with styles for the Tabbed Interface (Blue/Green/Orange themes).
    - [x] Create `labs/js/lab-switcher.js` to handle platform toggling.
- [x] **Task: Create Lab Template** <!-- cab1961 -->
    - [x] Build `labs/_template.html` containing the skeleton: Scenario -> Data Download -> Tabs -> Assessment.
    - [x] Create `labs/index.html` as the "Lab Manual" Table of Contents.

## Phase 2: Foundation Labs (Part I)
- [ ] **Task: Lab 01 - Data Models**
    - Topic: Exploring Vector vs Raster data.
    - Data: "Austin_Data.zip" (Roads.shp, Elevation.tif).
- [ ] **Task: Lab 02 - Map Design**
    - Topic: Symbology & Classification.
    - Data: "Texas_Counties.geojson" (Census data).
- [ ] **Task: Lab 03 - Projections**
    - Topic: Measuring Distortion.
    - Data: World Map (WGS84).

## Phase 3: Data & Remote Sensing Labs (Part II & III)
- [ ] **Task: Lab 04 - GPS/Import**
    - Topic: CSV to Point Map.
    - Data: "Campus_Trees.csv".
- [ ] **Task: Lab 05 - Georeferencing**
    - Topic: Image to Map.
    - Data: Historic Image JPG + Reference Vector.
- [ ] **Task: Lab 07 - Remote Sensing**
    - Topic: Band Combinations.
    - Data: Landsat 8 Scene (Bands 2-5).

## Phase 4: Analysis & Application (Part IV & V)
- [ ] **Task: Lab 08 - Site Selection**
    - Topic: Buffer & Overlay.
    - Data: "Suitable_Site_Project.gdb".
- [ ] **Task: Lab 10 - Storytelling**
    - Topic: Exporting & Web Presentation.
    - Data: Result from Lab 08.

## Phase 5: Integration
- [ ] **Task: Update Homepage**
    - Add a "Lab Manual" card/section to `index.html`.
    - Link individual chapters to their corresponding labs.
- [ ] **Task: Verify Mobile Responsiveness**
    - Ensure lab instructions are readable on phone/tablet.
