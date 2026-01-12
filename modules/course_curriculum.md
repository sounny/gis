# Geographic Information Systems & Remote Sensing

## A Comprehensive Digital Textbook Curriculum

---

## Course Overview

This curriculum synthesizes the rigorous academic framework from the **University of Florida's GIS5107C/3043** course with the applied research focus of **Southwestern GIS** blog case studies, all delivered through a modern, interactive digital textbook format.

**Course Philosophy**: Move beyond "button-clicking" GIS instruction to develop **spatial thinking** and **analytical reasoning** skills that enable students to solve real-world problems using geospatial technologies.

---

## Part I: Foundations of GIS & Spatial Data

### Module 00: Course Orientation

**Topics**:

- Welcome to GIS: History and Evolution
- GIS as Science vs. GIS as Tool (Debate)
- First Law of Geography (Tobler)
- Components of a GIS System
- Setting up your ArcGIS Pro/QGIS Environment

**Interactive Lab**: _Lab Setup & Your First Map_

- Create a simple map from scratch using ArcGIS Pro
- ESRI: Getting Started with GIS
- ESRI: Map Design Fundamentals

**Case Study**: _The Birth of GIS_ - John Snow's Cholera Map (1854)

---

### Module 01: What is Spatial Data?

**Topics**:

- The GIS Data Model: How computers represent the real world
- Vector Data Model: Points, Lines, Polygons
- Raster Data Model: Pixels and Grids
- Emerging Data Models (TINs, 3D, Point Clouds)
- Attributes and Attribute Tables
- Data Formats: Shapefiles, GeoJSON, GeoTIFF, KML

**Interactive Lab**: _Geocoding & Mapping Disaster Trends_

- Using the EM-DAT disaster database
- Geocoding historical events

**Case Study from Southwestern GIS**:

- _Voter Migration and the Geographic Sorting of the American Electorate_ - Understanding spatial patterns in voting behavior
- _A GIS-based spatial analysis on neighborhood effects and voter turn-out_ (College Station, TX)

---

### Module 02: Map Elements & Cartographic Design

**Topics**:

- Essential Map Elements: Title, Legend, Scale Bar, North Arrow, Source
- Choropleth Mapping: Principles and Pitfalls
- Classification Methods: Equal Interval, Quantile, Natural Breaks
- Color Theory and Accessibility in Mapping
- The Ethics of Map Design

**Interactive Lab**: _Make A Simple Map_

- Building a publication-ready map in ArcGIS Pro

**Interactive Tool**: 🎨 **The Color Bias Simulator**

- Explore how color choices can manipulate perception of spatial data

---

### Module 03: Geodesy, Projections & Coordinate Systems

**Topics**:

- From Real Surface to Ellipsoid: Why the Earth isn't round
- Horizontal and Vertical Datums (WGS84, NAD83, NAVD88)
- Map Projections: Cylindrical, Conic, Azimuthal
- Projection Distortions: Conformal vs. Equal-Area
- Coordinate Systems: Geographic (Lat/Long) vs. Projected (UTM, State Plane)
- The Mercator Debate: Colonial Cartography and Modern Ethics

**Interactive Lab**: _Alaska vs. Texas - Does Projection Matter?_

- Calculate the "true" size of states using equal-area projections
- The True Size web application

**Interactive Tool**: 🌍 **The Projection Distortion Simulator**

- Drag countries to see how Mercator distorts at different latitudes

**Case Study**: _How Big is the Earth?_ - Eratosthenes' 3rd Century BCE calculation

---

### Module 04: GPS, Positioning & Geolocation

**Topics**:

- Introduction to GNSS: GPS, GLONASS, Galileo, BeiDou
- How GPS Works: Trilateration Basics
- Sources of GPS Error and DGPS
- Datum Transformations in the Field
- Consumer vs. Survey-Grade GPS
- Null Island and Common GPS Pitfalls

**Interactive Lab**: _GPS Long Lats of the SEC_

- Field collection of stadium coordinates
- Spatial Point Pattern Analysis

**Interactive Tool**: 📍 **The GPS Accuracy Visualizer**

- Simulate error sources affecting position accuracy

---

## Part II: Data Creation & Management

### Module 05: Georeferencing & Digitizing

**Topics**:

- What is Georeferencing? The Art of Locating Images
- Control Points and Transformation Methods (Affine, Polynomial, Spline)
- RMSE: Measuring Geometric Accuracy
- Digitizing: Creating Vector Data from Images
- GIS Data Quality and Error Propagation

**Interactive Lab**: _Georeferencing Historical Maps_

- Florida Historical Aerial Photo (APLUS)
- Digitizing features from scanned maps

**Interactive Tool**: 🗺️ **The Georeferencer Overlay**

- Slider comparison between historical map and modern imagery

**Case Study from Southwestern GIS**:

- _New York City: GIS Measures and Field Observation_ - Validating GIS data with ground truth

---

### Module 06: Database Management & Attribute Queries

**Topics**:

- What is the Census? Geographic Hierarchies
- Attribute Tables and Field Types
- SQL for Spatial Data: Select, Calculate, Join
- Geodatabases: Personal, File, Enterprise
- Table Joins and Relates: Connecting Spatial and Non-Spatial Data

**Interactive Lab**: _Mapping Census Data_

- TIGER/Line files and American Community Survey
- Hospital Accessibility Analysis in Wyoming

**Interactive Tool**: 💾 **The SQL Sandbox**

- Practice attribute queries in a browser-based environment

---

## Part III: Remote Sensing & Earth Observation

### Module 07: Foundations of Remote Sensing

**Topics**:

- The Electromagnetic Spectrum: Beyond Visible Light
- Spectral Signatures: How Different Materials Reflect Energy
- Passive vs. Active Remote Sensing
- Sensor Resolutions: Spatial, Spectral, Temporal, Radiometric
- Key Satellite Systems: Landsat, Sentinel, MODIS, Planet

**Interactive Lab**: _Spectral Indices (NDVI, NDWI, NBR)_

- Calculating vegetation health from Landsat imagery

**Interactive Tool**: 🔬 **The Spectrum Slider**

- Click on vegetation, water, soil to see their reflectance curves

**Case Study from Southwestern GIS**:

- _GIS Methods and Multi-Temporal Remote Sensing Data for Improved Landslide Hazard Mapping_ (Southern Kyrgyzstan)

---

### Module 08: Image Classification & Land Change Science

**Topics**:

- Digital Image Processing: Band Combinations and Enhancements
- Supervised vs. Unsupervised Classification
- Training Data and Accuracy Assessment (Confusion Matrices)
- Land Cover vs. Land Use: A Conceptual Distinction
- Land-Change Science: Detecting Environmental Transformation

**Interactive Lab**: _Land-cover Change Detection_

- Multi-temporal analysis of urban sprawl
- Identifying "before and after" using Sentinel-2

**Interactive Tool**: 🌆 **The Urban Sprawl Animator**

- Time-series classification visualization

**Case Study from Southwestern GIS**:

- _Land Changes Fostering Atlantic Forest Transition in Brazil: Evidence from the Paraíba Valley_
- _The Global Impact of Land-Use Change_ - Climate Change Implications

**Key Reading**: Turner, B. L., & Robbins, P. (2008). _Land-change science and political ecology._

---

### Module 09: LiDAR & 3D Data Analysis

**Topics**:

- What is LiDAR? Active Sensing with Lasers
- Point Clouds: The Raw LiDAR Product
- Creating DEMs, DSMs, and CHM (Canopy Height Models)
- Terrain Analysis: Slope, Aspect, Hillshade
- Applications: Forestry, Archaeology, Flood Modeling

**Interactive Lab**: _Canopy Height Modeling using NEON LiDAR_

- Deriving forest structure from point clouds

**Interactive Tool**: 🌲 **The LiDAR Point Cloud Explorer**

- Filter by return number, classify points

---

## Part IV: Spatial Analysis & Modeling

### Module 10: Raster Analysis Fundamentals

**Topics**:

- Map Algebra: The Language of Raster Analysis
- Local, Focal (Neighborhood), Zonal, and Global Operations
- Hydrological Analysis: Flow Direction, Watersheds, Stream Order
- Terrain Analysis: Slope, Aspect, Viewshed

**Interactive Lab**: _Spatial Interpolation_

- IDW, Kriging, and Spline methods
- Cross-validation and choosing the best method

**Interactive Tool**: 📊 **The Map Algebra Calculator**

- Visual representation of cell-by-cell operations

**Case Study from Southwestern GIS**:

- _Characterizing and Predicting Traffic Accidents in Extreme Weather Environments_

---

### Module 11: Vector Spatial Analysis

**Topics**:

- Spatial Analysis 101: Selection, Classification, Measurement
- Proximity Analysis: Buffers and Multi-Ring Buffers
- Overlay Analysis: Intersect, Union, Clip, Erase
- Network Analysis: Shortest Path, Service Areas

**Interactive Lab**: _John Snow Map - Spatial Analysis_

- Recreating the 1854 cholera investigation with modern tools
- Hospital Accessibility Analysis (Service Areas)

**Interactive Tool**: ⭕ **The Buffer Visualizer**

- See how buffer distances affect analysis outcomes

---

### Module 12: Introduction to Spatial Modeling

**Topics**:

- What are Models? Conceptual, Cartographic, and Mathematical
- ModelBuilder: Automating GIS Workflows
- Simple Suitability Analysis: Weighted Overlay
- Spatio-Temporal Models: Beyond Static Snapshots

**Interactive Lab**: _Building Geoprocessing Models using ArcGIS Pro_

- Chaining tools together for repeatable analysis

**Case Study from Southwestern GIS**:

- _Malaria diagnosis and mapping with m-Health and GIS: evidence from Uganda_
- _Summary of Technological Change and The Spatial Structure of Agriculture_

---

## Part V: Applied GIS & Capstone

### Module 13: Mobile GIS & Field Data Collection

**Topics**:

- Mobile GIS: From GPS to Smartphones
- ESRI Field Maps and Survey123
- Data Collection Protocols and Quality Control
- Citizen Science and Crowdsourced Geographic Information

**Interactive Lab**: _Field Data Collection Exercise_

- Create a survey, collect data, sync to ArcGIS Online

---

### Module 14: Storytelling with Maps

**Topics**:

- The Power of Spatial Narratives
- ArcGIS StoryMaps: Structure and Design
- Cartograms and Non-Traditional Visualizations
- Ethical Considerations in Map Communication

**Interactive Lab**: _Creating an Interactive StoryMap_

- Combining maps, media, and narrative

---

### Module 15: GIS Ethics, AI, and the Future

**Topics**:

- Bias in Spatial Algorithms: Redlining to Predictive Policing
- GeoAI: Machine Learning in Spatial Analysis
- Privacy and Location Data
- Open Data vs. Proprietary Systems
- The Future of Earth Observation

**Guest Lecture/Reading**: Contemporary issues in GeoAI

---

### Module 16: Final Project

**Project Phases**:

1. **Proposal** - Define research question, data sources, methods
2. **Check-in** - Progress review with instructor
3. **Poster** - Scientific poster presentation

**Resources**:

- GIS and Remote Sensing Data Sources Guide
- Poster Design Best Practices

**Student Poster Examples** (from UF & SU):

- Coffee Shops Location Analysis
- Apple Snail Habitat Modeling
- Cool Roofs and Urban Heat
- Historical Map Digitization
- Mental Health Access Mapping
- Farmer's Market Accessibility
- Pedestrian Safety Analysis

---

## Course Assessments

### Weekly Quizzes

- What is GIS? The Quiz
- Spatial Data Quiz
- Projections Lecture Quiz
- GPS Lecture Quiz
- Georeferencing Lecture Quiz
- Remote Sensing Lecture Quiz
- Raster Analysis Quiz
- Spatial Analysis Quiz

### Final Exams

1. **GIS Conceptual Exam** - Understanding core concepts
2. **GIS Lab Practical** - Hands-on skills assessment
3. **Acronyms Quiz** - Mastering the language of GIS

---

## Interactive Learning Tools Summary

| Module | Interactive Tool                   | Description                                          |
| ------ | ---------------------------------- | ---------------------------------------------------- |
| 01     | 🔬 Spectrum Slider                 | Visualize spectral reflectance of different surfaces |
| 02     | 🎨 Color Bias Simulator            | Explore how color choices affect map perception      |
| 03     | 🌍 Projection Distortion Simulator | Compare projections in real-time                     |
| 04     | 📍 GPS Accuracy Visualizer         | Simulate error sources in positioning                |
| 05     | 🗺️ Georeferencer Overlay           | Compare historical and modern imagery                |
| 06     | 💾 SQL Sandbox                     | Practice database queries                            |
| 07     | 🔬 Spectrum Slider                 | Deep dive into spectral signatures                   |
| 08     | 🌆 Urban Sprawl Animator           | Time-series land change visualization                |
| 09     | 🌲 LiDAR Point Cloud Explorer      | Interactive 3D point cloud viewer                    |
| 10     | 📊 Map Algebra Calculator          | Visual raster operations                             |
| 11     | ⭕ Buffer Visualizer               | Interactive proximity analysis                       |

---

## Key Readings

1. **Tobler, W. (1970)**. _A computer movie simulating urban growth in the Detroit region._ Economic Geography, 46, 234-240.
2. **Turner, B. L., & Robbins, P. (2008)**. _Land-change science and political ecology: Similarities, differences, and implications for sustainability science._ Annual Review of Environment and Resources, 33, 295-316.
3. **Goodchild, M. F.** _GIS Modeling Overview_ (Course Reading)
4. **Dana, P. H. (1997)**. _GPS Overview_
5. **Zandbergen, P. A. (2009)**. _Accuracy of iPhone Locations._ TGIS
6. **ESRI**. _Understanding Map Projections_

---

## Data Sources

- **USGS EarthExplorer** - Landsat, NAIP, DEMs
- **Copernicus Open Access Hub** - Sentinel imagery
- **US Census Bureau** - TIGER/Line, ACS data
- **EM-DAT** - International Disaster Database
- **OpenStreetMap** - Crowdsourced vector data
- **NEON** - National Ecological Observatory Network (LiDAR)
- **Florida APLUS** - Historical aerial photography

---

## Course Timeline (15-Week Semester)

| Week | Module                   | Lab Assignment           |
| ---- | ------------------------ | ------------------------ |
| 1    | 00: Orientation          | Lab Setup                |
| 2    | 01: Spatial Data         | Geocoding                |
| 3    | 02: Map Design           | Simple Map               |
| 4    | 03: Projections          | Alaska vs Texas          |
| 5    | 04: GPS                  | SEC Coordinates          |
| 6    | 05: Georeferencing       | Historical Map           |
| 7    | 06: Databases            | Census Mapping           |
| 8    | **Midterm Review**       | Lab Practical 1          |
| 9    | 07: Remote Sensing       | Spectral Indices         |
| 10   | 08: Classification       | Change Detection         |
| 11   | 09: LiDAR                | Canopy Height            |
| 12   | 10: Raster Analysis      | Interpolation            |
| 13   | 11: Vector Analysis      | John Snow Map            |
| 14   | 12-14: Modeling & Ethics | Final Project            |
| 15   | **Finals Week**          | Poster & Conceptual Exam |

---

## Source Integration Notes

### From UF Canvas (GIS5107C/3043)

- 10-week modular structure with clear lecture/quiz/lab progression
- ESRI-pathway integration (Getting Started, Geodatabase, Coordinate Systems)
- ArcGIS Pro-centric instruction with emphasis on data management
- Robust assessment strategy (weekly quizzes, practical exams)

### From Southwestern GIS Blog

- Real-world application case studies for each module
- Emphasis on spatial analysis in social science contexts (voting, health, agriculture)
- Remote sensing applications (landslide mapping, land change, climate)
- Student poster examples demonstrating breadth of GIS applications

### Development Focus

- Interactive learning tools built with Vanilla JS/CSS
- RS-forward curriculum integrated throughout
- Research themes: Sustainability, Placemaking, Environmental Impact

---

_Last Updated: January 2026_
_Course Design: Dr. Moulay Anwar Sounny-Slitine_
