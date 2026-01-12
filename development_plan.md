# GIS Digital Textbook: Implementation Plan

This document outlines the strategic plan for developing the **"Geographic Information Systems & Remote Sensing"** digital textbook, synthesizing:

- **UF Canvas GIS5107C/3043** structured course content
- **Southwestern GIS** blog case studies and research applications
- Dr. Sounny's research themes in sustainability and spatial analysis

---

## 1. Core Principles

- **Dual-Platform Learning**: ArcGIS Pro for industry skills + Google Earth Engine for RS/cloud computing
- **Research-Integrated**: Every module connects to real-world case studies from published research
- **Interactive-First**: Custom JS/CSS simulations replace static diagrams
- **Aesthetic Excellence**: Premium design following "Antigravity" standards
- **Open & Accessible**: Brand-neutral OER following accessibility guidelines

---

## 2. Comprehensive Curriculum (17 Modules)

### Part I: Foundations of GIS & Spatial Data

| Module | Title                 | UF Canvas Source       | Southwestern GIS Case Study          |
| ------ | --------------------- | ---------------------- | ------------------------------------ |
| **00** | Course Orientation    | Week 0: Introduction   | John Snow Cholera Map                |
| **01** | What is Spatial Data? | Week 2: Spatial Data   | Voter Migration & Geographic Sorting |
| **02** | Map Elements & Design | Week 1: Welcome to GIS | —                                    |
| **03** | Geodesy & Projections | Week 3: Projections    | —                                    |
| **04** | GPS & Positioning     | Week 4: GPS/Long-Lats  | —                                    |

### Part II: Data Creation & Management

| Module | Title                       | UF Canvas Source        | Southwestern GIS Case Study |
| ------ | --------------------------- | ----------------------- | --------------------------- |
| **05** | Georeferencing & Digitizing | Week 5: Georeferencing  | NYC Field Observation       |
| **06** | Database Management         | Week 8: Database/Census | —                           |

### Part III: Remote Sensing & Earth Observation

| Module | Title                              | UF Canvas Source       | Southwestern GIS Case Study           |
| ------ | ---------------------------------- | ---------------------- | ------------------------------------- |
| **07** | Foundations of Remote Sensing      | Week 6: Remote Sensing | Landslide Hazard Mapping (Kyrgyzstan) |
| **08** | Image Classification & Land Change | Week 7: Classification | Atlantic Forest Transition (Brazil)   |
| **09** | LiDAR & 3D Analysis                | Week 9: Raster/LiDAR   | —                                     |

### Part IV: Spatial Analysis & Modeling

| Module | Title                   | UF Canvas Source          | Southwestern GIS Case Study          |
| ------ | ----------------------- | ------------------------- | ------------------------------------ |
| **10** | Raster Analysis         | Week 9: Raster Analysis   | Traffic Accidents in Extreme Weather |
| **11** | Vector Spatial Analysis | Week 10: Spatial Analysis | —                                    |
| **12** | Spatial Modeling        | Week 10: Interpolation    | Malaria Mapping (Uganda)             |

### Part V: Applied GIS & Capstone

| Module | Title                   | UF Canvas Source | Southwestern GIS Case Study |
| ------ | ----------------------- | ---------------- | --------------------------- |
| **13** | Mobile GIS & Field Data | —                | —                           |
| **14** | Storytelling with Maps  | —                | —                           |
| **15** | GIS Ethics & AI         | —                | —                           |
| **16** | Final Project           | Final Project    | Student Poster Examples     |

**Full curriculum document**: See `modules/course_curriculum.md`

---

## 3. Development Phases

### Phase 1: Foundation (Weeks 1-3)

**Status**: 🟡 In Progress

- [x] Create `development_plan.md` and `course_curriculum.md`
- [x] Build interactive module templates (Module 01, 02)
- [ ] Finalize `css/style.css` design system with all tokens
- [ ] Create navigation shell for 17-module structure
- [ ] Set up `data/` folder structure for lab datasets

### Phase 2: Part I - Foundations (Weeks 4-7)

**Target**: Modules 00-04

- [ ] Module 00: Welcome video + Lab Setup walkthrough
- [ ] Module 01: Spectrum Slider (✓ Complete), Geocoding lab
- [ ] Module 02: Band Combiner interactive (✓ Complete)
- [ ] Module 03: Projection Distortion Simulator
- [ ] Module 04: GPS Accuracy Visualizer

### Phase 3: Part II & III - RS Focus (Weeks 8-12)

**Target**: Modules 05-09

- [ ] Module 05: Georeferencer Overlay tool
- [ ] Module 06: SQL Sandbox browser tool
- [ ] Module 07: Deep-dive Spectral Signature explorer
- [ ] Module 08: Land Change time-lapse animator
- [ ] Module 09: LiDAR Point Cloud WebGL viewer

### Phase 4: Part IV - Analysis (Weeks 13-16)

**Target**: Modules 10-12

- [ ] Module 10: Map Algebra visual calculator
- [ ] Module 11: Buffer/Overlay analysis tool
- [ ] Module 12: ModelBuilder simulation

### Phase 5: Capstone & Polish (Weeks 17-20)

**Target**: Modules 13-16 + Final QA

- [ ] Module 13-15: Applied topics content
- [ ] Module 16: Final Project guidelines + rubric
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] SEO optimization for all pages
- [ ] Cross-browser testing

---

## 4. Interactive Tools Inventory

| Module | Tool Name                 | Status      | Tech Stack          |
| ------ | ------------------------- | ----------- | ------------------- |
| 01     | 🔬 Spectrum Slider        | ✅ Complete | Vanilla JS/CSS      |
| 02     | 🎨 Band Combiner          | ✅ Complete | Vanilla JS/CSS      |
| 03     | 🌍 Projection Simulator   | 📋 Planned  | Leaflet + D3.js     |
| 04     | 📍 GPS Visualizer         | 📋 Planned  | Canvas API          |
| 05     | 🗺️ Georeferencer Overlay  | 📋 Planned  | Leaflet             |
| 06     | 💾 SQL Sandbox            | 📋 Planned  | sql.js (WASM)       |
| 08     | 🌆 Land Change Animator   | 📋 Planned  | Canvas + GeoTIFF.js |
| 09     | 🌲 LiDAR Explorer         | 📋 Planned  | Three.js/WebGL      |
| 10     | 📊 Map Algebra Calculator | 📋 Planned  | Vanilla JS          |
| 11     | ⭕ Buffer Visualizer      | 📋 Planned  | Turf.js             |

---

## 5. Assessment Framework

### Weekly Assessments

| Quiz                 | Associated Module |
| -------------------- | ----------------- |
| What is GIS?         | Module 00         |
| Spatial Data Quiz    | Module 01         |
| Projections Quiz     | Module 03         |
| GPS Quiz             | Module 04         |
| Georeferencing Quiz  | Module 05         |
| Remote Sensing Quiz  | Module 07         |
| Raster Analysis Quiz | Module 10         |
| Acronyms Quiz        | Final Review      |

### Practical Exams

1. **Lab Practical 1** (Midterm): Modules 00-06
2. **Lab Practical 2** (Final): Modules 07-12
3. **Conceptual Exam**: Full course concepts

### Final Project

- Proposal → Check-in → Poster submission
- Rubric aligned with professional conference standards

---

## 6. Key Readings & References

### From UF Canvas Course Materials

- Module PDFs (Spatial Data, Projections, Remote Sensing, etc.)
- ESRI Training pathways

### From Southwestern GIS Blog

- Voter Migration spatial analysis
- Landslide hazard mapping with RS
- Atlantic Forest land change
- m-Health malaria mapping
- Traffic accident prediction

### Academic Foundations

- Tobler (1970) - First Law of Geography
- Turner & Robbins (2008) - Land-change science
- Goodchild - GIS Modeling Overview

---

## 7. Data Assets Required

| Lab            | Dataset                 | Source             | Status     |
| -------------- | ----------------------- | ------------------ | ---------- |
| Geocoding      | US Disaster Events      | EM-DAT             | 📋 Pending |
| Projections    | US States Boundaries    | Census TIGER       | 📋 Pending |
| GPS            | SEC Stadium Coordinates | Manual collection  | 📋 Pending |
| Remote Sensing | Landsat 8/9 Scene       | USGS EarthExplorer | 📋 Pending |
| Land Change    | Sentinel-2 Time Series  | Copernicus Hub     | 📋 Pending |
| LiDAR          | NEON Point Cloud        | NEON Data Portal   | 📋 Pending |
| Census         | ACS 5-Year              | Census API         | 📋 Pending |

---

_Last Updated: January 11, 2026_
_Version: 2.0 - Full Curriculum Integration_
