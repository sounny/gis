# GIS Digital Textbook: Implementation Plan

This document outlines the strategic plan for developing the "Geographic Information Systems" digital textbook, bridging legacy course materials from _Southwestern GIS_ with modern standards and Dr. Sounny's research themes.

## 1. Core Principles

- **Modernize**: Transition from legacy vector GIS to a **Remote Sensing-integrated workflow** using ArcGIS Pro, QGIS, and Google Earth Engine.
- **Aesthetic First**: Adhere to "Antigravity" design standards (high premium, modern typography, dynamic UI).
- **RS-Applied Learning**: Use Earth Observation case studies (Flood mapping, Wildfire monitoring, Land Use Change) as lab foundations.
- **Research-Driven**: Integrate themes of _Placemaking_, _Sustainability_, and _Environmental Impact_ using RS metrics.

## 2. Content Migration Map

| New Module | Topic                          | Legacy Lab Reference (Southwestern GIS) | Research Integration Theme             |
| :--------- | :----------------------------- | :-------------------------------------- | :------------------------------------- |
| **01**     | Orientation & Spatial Thinking | Lab 1: Getting Started                  | Architectural History (Place vs Space) |
| **02**     | Map Elements & Design          | Lab 2-5: Cartography Basics             | Aesthetic Ethics in Cartography        |
| **03**     | Working with GIS Data          | Lab 7: Queries, Lab 9: Joins            | Data Sovereignty & Sustainability      |
| **04**     | Geocoding Addresses            | _New/Refined Lab_                       | Placemaking: Defining Home/Work        |
| **05**     | Georeferencing Imagery         | Lab 8: Georeferencing                   | Historical Evolution of the Workplace  |
| **06**     | Modern Web Mapping             | _New focus on AGOL/Leaflet_             | Hybrid Work & Digital Third Places     |
| **09**     | Basic Spatial Analysis         | Lab 12: Projections, Lab 13: Floods     | Sustainability & Risk Assessment       |
| **10**     | Vector Analysis                | Lab 14: Tornados, Lab 18: Race          | Placemaking: Equitable Design          |
| **11**     | Raster Analysis                | Lab 16: Raster, Lab 22: Remote Sensing  | IPAT Equation: Environmental Impact    |
| **12**     | Network Analysis               | _New focus on Transportation_           | Workplace Accessibility & Mobility     |

## 3. Development Phases

### Phase 1: Foundation (Weeks 1-2)

- [ ] Finalize `index.html` (Coming Soon) and `css/style.css` design tokens.
- [ ] Create template for Chapter/Module pages with consistent navigation.
- [ ] Establish folder structure for Lab Assets (data, instructions).

### Phase 2: Core Modules (Weeks 3-8)

- [ ] **Module 01-02**: Develop intro content using modern ArcGIS Pro interface.
- [ ] **Module 05 (Georeferencing)**: Implement the historical imagery lesson using Central Texas data.
- [ ] **Module 03-04**: Build out data management labs with a focus on public datasets (TIGER, OpenData portals).

### Phase 4: Analysis & Modeling (Weeks 9-12)

- [ ] **Module 10 (Vector)**: Port the Tornado and Flood modeling labs to ArcGIS Pro.
- [ ] **Module 11 (Raster)**: Port NDVI and Image Classification labs.
- [ ] **Module 06**: Create a "No-Code" web mapping tutorial.

### Phase 5: Finalization (Weeks 13-15)

- [ ] Develop the Final Project prompt.
- [ ] Final SEO and accessibility audit.
- [ ] "Go-Live" launch.

## 5. Interactive Learning Strategy (The RS Focus)

Every module will feature a custom, interactive simulation built with **Vanilla JS/CSS** that specifically targets **Remote Sensing** principles.

### Planned Interactive Tools:

1. **Module 01: The Spectrum Slider** - Visualize how different objects (water, vegetation, soil) reflect light across the electromagnetic spectrum.
2. **Module 02: Band Combiner** - An interactive "Digital Sensor" where students combine R, G, B, and NIR bands to create True Color and False Color composites.
3. **Module 03: Resolution Matcher** - Visualizing the trade-offs between Spatial, Temporal, and Spectral resolution.
4. **Module 05: The Georeferencer Overlay** - A slider comparison between a historical map and modern high-res satellite imagery.
5. **Module 09: Fire Progression Simulator** - Use temporal imagery to visualize how a wildfire spreads and how we detect "Burn Scars" using NBR.
6. **Module 11: Vegetation Index Lab** - Interactive NDVI calculator where users drag "pixels" of different health into a formula box.
7. **Module 16: AI Feature Extractor** - A simulation of how Deep Learning identifies building footprints from coarse imagery.

## 6. Curated Content Expansion

To provide a more comprehensive curriculum, we will expand the module list to include:

- **Module 16: GIS Ethics & AI** - Discussing bias in spatial algorithms and the future of GeoAI.
- **Module 17: Mobile GIS** - Practical guide to Field Maps and Survey123.
- **Module 18: Storytelling with Maps** - Mastering ArcGIS StoryMaps and digital narratives.
- **Module 19: Cartograms & Data Viz** - Non-traditional spatial representations.
