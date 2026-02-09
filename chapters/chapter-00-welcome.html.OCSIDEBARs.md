# OCSIDEBARs: chapter-00-welcome.html

Page title: Chapter 00: Welcome to GIS | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-00-welcome.html`

## Concepts (for context)
- layer
- raster
- vector
- coordinate reference system (CRS)
- remote sensing
- area of interest (AOI)
- Stop &amp; check
- Lab (Three Tracks)
- What is GIS?
- Asking the Questions of "Where"
- The Art of GIS
- GIS in Action: Case Studies
- 1. Sustainability: Are Solar Panels Enough?
- 2. Physical Geography: Inverting the Landscape
- 3. Humanities: Where is the "Southwest"?
- Case Study: Asking the Questions of "Where"
- -  The GIS Learning Journey
- Spatial Thinking Pre-Check
- Learning Objectives
- Master Remote Sensing
- Spatial Analysis
- Cartographic Design
- Software Toolkit
- Desktop & Cloud Engines
- WebGIS Applications
- AI-Assisted Workflows
- Tips for Success
- Gerardus Mercator
- Texas Connection
- Florida Connection
- (truncated) total concepts detected: 33

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 00: Welcome to GIS (00 welcome), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-020.md` (signal=5)
  oducing raster output, the device target, such as print, screen display, and the map content, should be considered when making a choice of raster format to use. This entry covers the primary raster formats applicable to cartography, considerations when using t...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=4)
  an></p> <figure class="image"><img alt="linear streets after rasterized" height="505" src="https://bok-figures.s3.amazonaws.com/files/DM86_Fig2_combined.png" width="457" /> <figcaption>Figure 2. A linear street network symbolized via functional class specifica...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-007.md` (signal=1)
  </strong>: Object-like data, in which the spatial extent or boundaries of the features are definable.</p> <p><strong>extent</strong>:&nbsp;The area or distance in real space over which some geographic entity exists. In cartography and GIS, the extent of a repr...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-data-models-for-gis.html` (signal=1)
  dels tend to be better representations of reality due to the accuracy and precision of points, lines, and polygons over the regularly spaced grid cells of the raster model. This results in vector data tending to be more aesthetically pleasing than raster data....

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 00: Welcome to GIS (00 welcome), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=131)
  # PD-05-033 - GDAL/OGR and Geospatial Data IO Libraries Source: https://gistbok-ltb.ucgis.org/page/34/concept/10769 ## Introduction <p>Qin, C-Z. and Zhu, L-J. (2020).&nbsp;GDAL/OGR and Geospatial Data IO Libraries.&nbsp;&nbsp;The Geographic Inform
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (signal=67)
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Geospatial Data Management</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s08-data-...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-data-models-for-gis.html` (signal=59)
  class="navbar-part middle"> <a href="index.html"><img src="shared/images/batch-up.png"></a> <a href="index.html">Table of Contents</a> </div> <div class="navbar-part right"> <a href="s09-geospatial-data-management.html">Next Chapter</a> <a href="s09-geospatial...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=54)
  p; Technology Body of Knowledge (2024 Edition), John P. Wilson (Ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2024.1.7" target="_blank">10.22224/gistbok/2024.1.7</a></p> ## Description <p><span><span><span>Spatial data can be represented in vector ...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 00: Welcome to GIS (00 welcome) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=5)
  in querying a raster layer based on its attribute values and are always used in tandem with Boolean operators. For example, to answer the first question in Table 3 &ldquo;Which areas have high population density AND low disaster frequency?&rdquo;, we can first...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=2)
  ch land parcels are for sale and which are zoned for commercial development. After collecting and overlaying the baseline information on available development zones, you can begin to determine which areas offer the most economic opportunity by collecting regio...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-02-multiple-layer-analysis.html` (signal=2)
  ch land parcels are for sale and which are zoned for commercial development. After collecting and overlaying the baseline information on available development zones, you can begin to determine which areas offer the most economic opportunity by collecting regio...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=1)
  "section_12/6770c44b59bc1b4b7875605be3ac21b0.jpg"> </div> <p class="para editable block" id="campbell_1.0-ch08_s02_s03_p02">Zonal operations and analyses are valuable in fields of study such as landscape ecology where the geometry and spatial arrangement of ha...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (texas_signal=1)
  <td>Introductory Physical Education</td> <td>10045</td> <td>23</td> </tr> <tr> <td>Harrison</td> <td>Auto Repair and Feminism</td> <td>10045</td> <td>54</td> </tr> <tr>

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=192)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=174)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=162)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-data-models-for-gis.html` (signal=145)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=142)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=141)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-02-multiple-layer-analysis.html` (signal=126)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-020.md` (signal=121)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-01-raster-data-models.html` (signal=95)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-007.md` (signal=76)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-01-basic-geoprocessing-with-raste.html` (signal=73)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (signal=69)
