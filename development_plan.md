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

## 2. Comprehensive Curriculum (21 Chapters)

### Part I: Foundations of GIS & Spatial Data

| Module | Title                                     | UF Canvas Source       | Southwestern GIS Case Study          |
| ------ | ----------------------------------------- | ---------------------- | ------------------------------------ |
| **00** | Course Orientation                        | Week 0: Introduction   | John Snow Cholera Map                |
| **01** | Spatial Thinking & Geographic Concepts    | Week 1: Welcome to GIS | —                                    |
| **02** | Maps and Cartographic Design              | Week 1: Welcome to GIS | —                                    |
| **03** | Geodesy, Projections & Coordinate Systems | Week 3: Projections    | —                                    |
| **04** | GPS & Positioning                         | Week 4: GPS/Long-Lats  | —                                    |

### Part II: GIS Data Models and Management

| Module | Title                                 | UF Canvas Source        | Southwestern GIS Case Study          |
| ------ | ------------------------------------- | ----------------------- | ------------------------------------ |
| **05** | Geospatial Data Models                | Week 2: Spatial Data    | Voter Migration & Geographic Sorting |
| **06** | Georeferencing and Digitizing         | Week 5: Georeferencing  | NYC Field Observation                |
| **07** | Database Management and Attribute Data | Week 8: Database/Census | —                                   |

### Part III: Remote Sensing & Earth Observation

| Module | Title                                    | UF Canvas Source       | Southwestern GIS Case Study           |
| ------ | ---------------------------------------- | ---------------------- | ------------------------------------- |
| **08** | Foundations of Remote Sensing            | Week 6: Remote Sensing | Landslide Hazard Mapping (Kyrgyzstan) |
| **09** | Working with Satellite Imagery           | Week 6: Remote Sensing | —                                     |
| **10** | Image Classification & Land Cover Mapping | Week 7: Classification | Atlantic Forest Transition (Brazil)  |
| **11** | LiDAR & 3D Data Analysis                 | Week 9: Raster/LiDAR   | —                                     |

### Part IV: Spatial Analysis & Modeling

| Module | Title                                   | UF Canvas Source          | Southwestern GIS Case Study          |
| ------ | --------------------------------------- | ------------------------- | ------------------------------------ |
| **12** | Raster Analysis & Map Algebra            | Week 9: Raster Analysis   | Traffic Accidents in Extreme Weather |
| **13** | Vector Analysis Operations               | Week 10: Spatial Analysis | —                                    |
| **14** | Spatial Interpolation & Geostatistics    | Week 10: Interpolation    | Malaria Mapping (Uganda)             |
| **15** | Spatial Modeling with ModelBuilder & Scripts | Week 10: Modeling    | —                                    |

### Part V: Applied GIS & Professional Practice

| Module | Title                                | UF Canvas Source | Southwestern GIS Case Study |
| ------ | ------------------------------------ | ---------------- | --------------------------- |
| **16** | Mobile GIS & Field Data Collection   | —                | —                           |
| **17** | Web Mapping and Storytelling         | —                | —                           |
| **18** | GIS Ethics, Privacy, and AI          | —                | —                           |
| **19** | GIS Project Management and Careers   | —                | —                           |
| **20** | Final Project - Research Poster      | Final Project    | Student Poster Examples     |

**Full curriculum documents**: See `chapters/COMPREHENSIVE_TOC.md` and `chapters/course_curriculum.md`

---

## 3. Development Phases

### Phase 1: Foundation (Weeks 1-3)

**Status**: 🟡 In Progress

- [x] Create `development_plan.md` and `course_curriculum.md`
- [x] Build interactive module templates (Chapters 00-02)
- [ ] Finalize `css/style.css` design system with all tokens
- [ ] Create navigation shell for 21-chapter structure
- [ ] Set up `data/` folder structure for lab datasets

### Phase 2: Part I - Foundations (Weeks 4-7)

**Target**: Chapters 00-04

- [ ] Chapter 00: Welcome video + Lab Setup walkthrough
- [ ] Chapter 01: Spatial Thinking interactive (mental map)
- [ ] Chapter 02: Map design lab + Color Bias interactive
- [ ] Chapter 03: Projection Distortion Simulator
- [ ] Chapter 04: GPS Accuracy Visualizer

### Phase 3: Part II & III - Data Models + Remote Sensing (Weeks 8-12)

**Target**: Chapters 05-11

- [ ] Chapter 05: Raster/Vector data model interactive
- [ ] Chapter 06: Georeferencer Overlay tool
- [ ] Chapter 07: SQL Sandbox browser tool
- [ ] Chapter 08: Deep-dive Spectral Signature explorer
- [ ] Chapter 09: Satellite imagery workflow (band combinations + indices)
- [ ] Chapter 10: Land Change time-lapse animator
- [ ] Chapter 11: LiDAR Point Cloud WebGL viewer

### Phase 4: Part IV - Analysis (Weeks 13-16)

**Target**: Chapters 12-15

- [ ] Chapter 12: Map Algebra visual calculator
- [ ] Chapter 13: Buffer/Overlay analysis tool
- [ ] Chapter 14: Interpolation method comparison tool
- [ ] Chapter 15: ModelBuilder simulation

### Phase 5: Capstone & Polish (Weeks 17-20)

**Target**: Chapters 16-20 + Final QA

- [ ] Chapters 16-19: Applied topics content
- [ ] Chapter 20: Final Project guidelines + rubric
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] SEO optimization for all pages
- [ ] Cross-browser testing

---

## 4. Interactive Tools Inventory

| Module | Tool Name                         | Status      | Tech Stack          |
| ------ | --------------------------------- | ----------- | ------------------- |
| 02     | 🎨 Color Bias Simulator           | 📋 Planned  | Vanilla JS/CSS      |
| 03     | 🌍 Projection Simulator           | ✅ Complete | Leaflet + D3.js     |
| 04     | 📍 GPS Visualizer                 | 📋 Planned  | Canvas API          |
| 06     | 🗺️ Georeferencer Overlay          | 📋 Planned  | Leaflet             |
| 07     | 💾 SQL Sandbox                    | 📋 Planned  | sql.js (WASM)       |
| 08     | 🔬 Spectrum Slider                | ✅ Complete | Vanilla JS/CSS      |
| 09     | 🎨 Band Combiner                  | ✅ Complete | Vanilla JS/CSS      |
| 10     | 🌆 Land Change Animator           | 📋 Planned  | Canvas + GeoTIFF.js |
| 11     | 🌲 LiDAR Explorer                 | 📋 Planned  | Three.js/WebGL      |
| 12     | 📊 Map Algebra Calculator         | 📋 Planned  | Vanilla JS          |
| 13     | ⭕ Buffer Visualizer              | 📋 Planned  | Turf.js             |

---

## 5. Assessment Framework

### Weekly Assessments

| Quiz                         | Associated Module |
| ---------------------------- | ----------------- |
| Course Orientation Quiz      | Module 00         |
| Spatial Thinking Quiz        | Module 01         |
| Cartographic Design Quiz     | Module 02         |
| Projections Quiz             | Module 03         |
| GPS Quiz                     | Module 04         |
| Geospatial Data Models Quiz  | Module 05         |
| Database Management Quiz     | Module 07         |
| Remote Sensing Quiz          | Module 08         |
| Raster Analysis Quiz         | Module 12         |
| Vector Analysis Quiz         | Module 13         |
| Acronyms Quiz                | Final Review      |

### Practical Exams

1. **Lab Practical 1** (Midterm): Modules 00-07
2. **Lab Practical 2** (Final): Modules 08-15
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
