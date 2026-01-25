# OCSIDEBARs: chapter-01-spatial-data.html

Page title: Chapter 01: What is Spatial Data? | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-01-spatial-data.html`

## Concepts (for context)
- vector
- raster
- pixel
- resolution
- extent
- topology
- ${icon} Best Choice: ${type.toUpperCase()}
- Stop &amp; check
- The Two Pillars of GIS
- Vector Model
- Raster Model
- Data Capture: Digitizing
- Manual GIS: The Legacy of Dr. John Snow
- Interactive Explorer: Choosing Your Model
- Interactive: The Data Model Decision Matrix
- Chapter 01 Checkpoint
- Roger Tomlinson
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 01: What is Spatial Data? (01 spatial data), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-020.md` (signal=5)
  oducing raster output, the device target, such as print, screen display, and the map content, should be considered when making a choice of raster format to use. This entry covers the primary raster formats applicable to cartography, considerations when using t...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-003.md` (signal=5)
  ping services can consume and convert shapefiles</td> <td style="vertical-align:top"> <ul> <li>Has indexing</li> <li>Preserves geometric accuracy</li> <li>No topology</li> <li>Good for static/print cartography</li> <li>Not usable in web/mobile maps</li> <li>Ha...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=4)
  an></p> <figure class="image"><img alt="linear streets after rasterized" height="505" src="https://bok-figures.s3.amazonaws.com/files/DM86_Fig2_combined.png" width="457" /> <figcaption>Figure 2. A linear street network symbolized via functional class specifica...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-007.md` (signal=1)
  </strong>: Object-like data, in which the spatial extent or boundaries of the features are definable.</p> <p><strong>extent</strong>:&nbsp;The area or distance in real space over which some geographic entity exists. In cartography and GIS, the extent of a repr...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 01: What is Spatial Data? (01 spatial data), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=131)
  # PD-05-033 - GDAL/OGR and Geospatial Data IO Libraries Source: https://gistbok-ltb.ucgis.org/page/34/concept/10769 ## Introduction <p>Qin, C-Z. and Zhu, L-J. (2020).&nbsp;GDAL/OGR and Geospatial Data IO Libraries.&nbsp;&nbsp;The Geographic Inform
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-003.md` (signal=70)
  eased, we are not only seeing an increase in available data, but also an increase in available data formats. Cartographers today have access to a wide range of interesting datasets, and online portals for downloading geospatial data now frequently offer that d...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (signal=67)
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Geospatial Data Management</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s08-data-...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-data-models-for-gis.html` (signal=59)
  class="navbar-part middle"> <a href="index.html"><img src="shared/images/batch-up.png"></a> <a href="index.html">Table of Contents</a> </div> <div class="navbar-part right"> <a href="s09-geospatial-data-management.html">Next Chapter</a> <a href="s09-geospatial...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 01: What is Spatial Data? (01 spatial data) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=5)
  in querying a raster layer based on its attribute values and are always used in tandem with Boolean operators. For example, to answer the first question in Table 3 &ldquo;Which areas have high population density AND low disaster frequency?&rdquo;, we can first...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-021.md` (signal=3)
  esolution of the object. Like &ldquo;scale&rdquo;, &ldquo;resolution&rdquo; is foundational and central to the study of geography and GIScience, as well as disciplines employing spatial data and spatial analysis such as ecology and environmental health science...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-003.md` (signal=2)
  e="vertical-align:top">Data (geospatial and non-geospatial) aggregated from a variety of government sources (including local governments).</td> <td style="vertical-align:top">Local government, agriculture, education, climate, disasters, manufacturing, maritime...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=1)
  "section_12/6770c44b59bc1b4b7875605be3ac21b0.jpg"> </div> <p class="para editable block" id="campbell_1.0-ch08_s02_s03_p02">Zonal operations and analyses are valuable in fields of study such as landscape ecology where the geometry and spatial arrangement of ha...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (texas_signal=1)
  <td>Introductory Physical Education</td> <td>10045</td> <td>23</td> </tr> <tr> <td>Harrison</td> <td>Auto Repair and Feminism</td> <td>10045</td> <td>54</td> </tr> <tr>

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-data-models-for-gis.html` (signal=256)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=207)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-020.md` (signal=175)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=171)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-01-raster-data-models.html` (signal=149)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=128)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-007.md` (signal=127)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-021.md` (signal=123)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s08-02-vector-data-models.html` (signal=81)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=80)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s09-geospatial-data-management.html` (signal=77)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-02-003.md` (signal=67)
