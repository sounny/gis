# Geographic Information Systems (GIS) | Digital Textbook

An open-access, comprehensive digital textbook for Geographic Information Systems and Remote Sensing, authored by Dr. Moulay Anwar Sounny-Slitine.

## Overview

This project is an interactive textbook exploring spatial thinking and analytical cartography. It combines foundational GIS concepts with hands-on labs and browser-based interactives.

The curriculum synthesizes:
- UF Canvas GIS5107C/3043 structured course content
- Southwestern GIS blog case studies and research applications
- Research themes in sustainability and spatial analysis

## Features

- **Dual-Platform Learning**: Covers ArcGIS Pro and Google Earth Engine.
- **Interactive-First**: Includes tools, labs, and assessments.
- **Comprehensive Curriculum**: 23 chapters covering foundations, data creation, remote sensing, analysis, and applied GIS.
- **Open Access**: Brand-neutral OER resources.

## Table of Contents

### Part I: Foundations of GIS & Spatial Data
- Ch 00: Welcome to GIS
- Ch 01: What is Spatial Data?
- Ch 02: Map Elements & Design
- Ch 03: Geodesy & Projections
- Ch 04: GNSS and Positioning

### Part II: Data Creation & Management
- Ch 05: Spatial Analysis
- Ch 06: Output & Production
- Ch 07: Database Management
- Ch 08: Georeferencing (Advanced)

### Part III: Remote Sensing & Earth Observation
- Ch 09: Spectral Analysis
- Ch 10: Foundations of RS
- Ch 11: Image Classification
- Ch 12: LiDAR & 3D Analysis

### Part IV: Spatial Analysis & Modeling
- Ch 13: Raster Analysis
- Ch 14: Vector Spatial Analysis
- Ch 15: Spatial Modeling

### Part V: Applied GIS & Ethics
- Ch 16: Mobile GIS & Field Data
- Ch 17: Storytelling with Maps
- Ch 18: GIS Ethics & Critical GIS

### Part VI: Research & Data Management
- Ch 19: Research Data Management
- Ch 20: Research in GIS

### Part VII: The Future of GIS
- Ch 21: Artificial Intelligence
- Ch 22: VGI & NeoGeography
- Ch 23: Lifelong Learning

## Usage

### Viewing the Textbook
Since this is a static website, you can view it by simply opening `index.html` in your web browser.

### Directory Structure
- `assets/`: Images and other static assets.
- `chapters/`: HTML files for each chapter.
- `conductor/`: Administrative or instructor resources.
- `css/`: Stylesheets.
- `data/`: Data files for labs and exercises.
- `labs/`: Lab instructions and materials.
- `scripts/`: Python utility scripts for maintenance.
- `tests/`: Python unit tests.

### Development & Maintenance

The project includes Python scripts for maintenance tasks such as checking link integrity.

To run the link checker:
```bash
python3 scripts/check_links.py
```

To run tests:
```bash
python3 -m unittest discover tests
```

## Contributing

Contributions to improve the content, fix typos, or add new examples are welcome. Please ensure that any new links are valid and that the project structure is maintained.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Dr. Moulay Anwar Sounny-Slitine**
- [Website](https://sounny.github.io)
