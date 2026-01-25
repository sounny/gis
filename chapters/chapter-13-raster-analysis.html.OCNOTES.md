# OCNOTES: chapter-13-raster-analysis.html

Page title: Chapter 13: Raster Spatial Analysis | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-13-raster-analysis.html`

## Concepts found on page

- map algebra
- NoData
- resampling
- alignment
- focal/zonal operations
- Map Algebra
- Focal Operation
- Zonal Operation
- Raster Spatial Analysis
- 🧮 What is Map Algebra?
- The Four Scopes
- Interactive: Local Algebra (Add)
- C. Dana Tomlin

## Strongest reference sources (overall)

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (signal=94)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-02-scale-of-analysis.html` (signal=10)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=10)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=6)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-04-077.md` (signal=5)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (signal=5)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/bok-mapping.md` (signal=3)

## Candidate excerpts to adapt (verbatim seeds; paraphrase into the chapter)

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md`
  # AM-02-006 - Grid Operations and Map Algebra Source: https://gistbok-ltb.ucgis.org/page/34/concept/10457 ## Introduction <p>Mennis, J. (2022). Grid Operations and Map Algebra. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Quarter 2022 Edition). John P. Wilson (Ed.).&nbsp; DOI:<a href="https://doi.org/10.22224/gistbok/2022.3.1" target="_blank">10.22224/gistbok/2022.3.1</a></p> <p>Thi...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-02-scale-of-analysis.html`
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Scale of Analysis</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s12-01-basic-geoprocessing-with-raste.html"><img src="shared/images/batch-left.png"></a> <a href="s12-01-basic-geoprocessing-with-raste.html">Previous Section</a> </div> <div cla...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html`
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Geospatial Analysis II: Raster Data</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s11-geospatial-analysis-i-vector-o.html"><img src="shared/images/batch-left.png"></a> <a href="s11-geospatial-analysis-i-vector-o.html">Previous Chapter</a> </d...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md`
  # DM-06-088 - Coordinate Transformations Source: https://gistbok-ltb.ucgis.org/page/34/concept/10663 ## Introduction <p>Seong, J. C. (2023). Coordinate Transformations.&nbsp;The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(4th Quarter 2022 Edition), John P. Wilson (ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2023.1.2" target="_blank">10.22224/gistbok/2023.1.2. </a></p> <p>The ...

## Reference matches by concept (top hits)

### map algebra

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (matches=47)
  Excerpt: # AM-02-006 - Grid Operations and Map Algebra Source: https://gistbok-ltb.ucgis.org/page/34/concept/10457 ## Introduction <p>Mennis, J. (2022). Grid Operations and Map Algebra. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Qua...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (matches=2)
  Excerpt: logical operations with binary variables (true or false). Boolean algebra uses the logical operators (AND, OR, NOT, XOR), to determine whether a particular condition is true or false.</p> <p><strong>Map algebra: </strong>a framework to analyze gridded data val...

### NoData

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (matches=4)
  Excerpt: list of name/value pairs, which are split into several groups (called domains; Figure 2). These domains include the &ldquo;Default&rdquo; domain for recording items with well-defined semantics (e.g., NODATA values), the &ldquo;SUBDATASETS&rdquo; domain for rec...
- `C:/Users/sounn/Git/gis/references/CSI/GIS_Data_Lab_9/rcsoils.txt` (matches=1)
  Excerpt: ncols 86 nrows 247 xllcorner 728574.3125 yllcorner 2025533.625 cellsize 30 NODATA_value -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -9999 -999...

### resampling

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (matches=6)
  Excerpt: without the need for manual coordinate transformations by users. The coordinate transformation mechanisms for vector and raster datasets are different because the raster datasets require pixel value resampling during coordinate transformations. As a case study...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (matches=4)
  Excerpt: squared error (RMSE) between known (i.e., input at GCPs) locations and the locations estimated by the model.</p> <p>The three orders of polynomial warping are often conflated with a related process, resampling. Georeferencing processes simply estimate the loca...

### alignment

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (matches=5)
  Excerpt: Development History and Background</span></span></span></li> <li><span><span><span>Geospatial Workforce Development Programs, Activities, and Centers</span></span></span></li> <li><span><span><span>Alignment Between Educational Achievements and Workforce Skill...
- `C:/Users/sounn/Git/gis/references/bok-mapping.md` (matches=3)
  Excerpt: # GIS KOK / BoK2 Alignment Map (Working Draft) This document maps the GIS Online Textbook chapters to the GIS&T **Body of Knowledge** (often referred to as **BoK** / **BoK2**). It is intended as a _curriculum alignment backbone_: - Make chapter scope explicit ...

### Map Algebra

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (matches=47)
  Excerpt: # AM-02-006 - Grid Operations and Map Algebra Source: https://gistbok-ltb.ucgis.org/page/34/concept/10457 ## Introduction <p>Mennis, J. (2022). Grid Operations and Map Algebra. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Qua...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (matches=2)
  Excerpt: logical operations with binary variables (true or false). Boolean algebra uses the logical operators (AND, OR, NOT, XOR), to determine whether a particular condition is true or false.</p> <p><strong>Map algebra: </strong>a framework to analyze gridded data val...

### Focal Operation

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-098.md` (matches=1)
  Excerpt: ur period during a heavy storm and combine it with a flood zone raster dataset to compute the average precipitation that fell over a 24-hour period in each flood zone. Zonal operations are similar to focal operations, where the zones themselves stand in place ...

### Zonal Operation

- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-02-scale-of-analysis.html` (matches=10)
  Excerpt: rs within the extent of the window, while a small range indicates the lack of an edge.</p> </div> <div class="section" id="campbell_1.0-ch08_s02_s03"> <h2 class="title editable block">Zonal Operations</h2> <p class="para editable block" id="campbell_1.0-ch08_s...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (matches=10)
  Excerpt: rs within the extent of the window, while a small range indicates the lack of an edge.</p> </div> <div class="section" id="campbell_1.0-ch08_s02_s03"> <h2 class="title editable block">Zonal Operations</h2> <p class="para editable block" id="campbell_1.0-ch08_s...

## Proposed adaptation to the book (concrete next edits for another agent)

- Interactive module candidates:
  - Model picker: give 6 real questions (pipes, flood surface, landcover, parcels, temperature, crime points) and have students choose vector/raster + why; reveal tradeoffs (file size, topology, mixed pixels).
  - Suitability studio: weighted overlay sliders; show how weights change the final 'best site'; include an ethics prompt about who benefits.
- Local-to-Global sidebar: search within the listed reference sources for a Texas anchor (Houston, Galveston, Austin, DFW, Rio Grande, Permian Basin) and write a 120-180 word sidebar that ends with a global parallel.
- 'Important Persons' bio box: if any reference source includes an inventor/author tied to this topic, add a 1-paragraph bio + 3 bullets (impact, algorithm/idea, modern use).
- Critical GIS prompt: add 1 dilemma question connected to the chapter's primary dataset choice (scale, privacy, bias, uncertainty) and ask for a written justification.

## Completed Adaptations (January 2026)

- [x] **Interactive module:** "Interactive: Local Algebra (Add)" implemented.
- [x] **Local-to-Global:** Added "Texas Storm Surge Modeling (SLOSH)" sidebar.
- [x] **Important Persons:** Added Bio Box for C. Dana Tomlin (Father of Map Algebra).
- [x] **Critical GIS:** Added "The Bias of Weights" callout regarding suitability modeling.
