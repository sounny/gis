# OCSIDEBARs: chapter-08-georeferencing.html

Page title: Chapter 08: Georeferencing | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-08-georeferencing.html`

## Concepts (for context)
- ground control point (GCP)
- checkpoint
- residual
- RMSE
- affine transformation
- resampling
- world file
- Stop &amp; check
- What is Georeferencing?
- Ground Control Points (GCPs)
- Interactive: Georeferencing Simulator
- Measuring Error: RMS
- Chapter 08 Checkpoint
- Dr. Peter H. Dana
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 08: Georeferencing (08 georeferencing), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md` (signal=4)
  i> <li>Lesson 9: Linear Regression Foundations in PSU STAT 500 Applied Statistics: <a href="https://online.stat.psu.edu/stat500/lesson/9" target="_blank">https://online.stat.psu.edu/stat500/lesson/9</a></li> </ul> <p><symbol></symbol><symbol></symbol></p>
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats-2.html` (signal=1)
  known as a heightmap when representing elevation) or as a vector-based triangular irregular network (TIN). When you look at a Digital Elevation Model (DEM) on a map, you dont see a cell matrix. Instead, you see a layer symbolized by a color ramp.</p> <ul> <li>...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats.html` (signal=1)
  known as a heightmap when representing elevation) or as a vector-based triangular irregular network (TIN). When you look at a Digital Elevation Model (DEM) on a map, you dont see a cell matrix. Instead, you see a layer symbolized by a color ramp.</p> <ul> <li>...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=1)
  . Values of a and b are used to compute values of f, &epsilon;2, and &epsilon;&#39;2, which, individually, can be used to describe the noncircularity of an ellipsoid. The literature often interchanges e and &epsilon; as symbols representing eccentricity. Figur...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 08: Georeferencing (08 georeferencing), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-015.md` (signal=69)
  # PD-05-015 - R for Geospatial Analysis and Mapping Source: https://gistbok-ltb.ucgis.org/page/34/concept/10759 ## Introduction <p>Engel, C. (2019). R for Geospatial Analysis and Mapping.&nbsp;The Geographic Information Science &amp; Techno
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md` (signal=40)
  224/gistbok/2025.1.10" target="_blank">10.22224/gistbok/2025.1.10</a></p> ## Description <p><span><span>Polynomial functions are one of many functions used to model global trends across one or n-dimensional spaces. In spatial analysis, polynomial functions are...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md` (signal=40)
  ="_blank">10.22224/gistbok/2024.1.11</a>.</p> ## Description <p>Regression analysis is a common statistical tool used to model relationships between variables and to explore the influencing factors underlying observed spatial data patterns. This entry focuses ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=18)
  /li> <li>Modern 3-D Geometric Terrestrial Reference Systems</li> </ol> <p>&nbsp;</p> <p><a><strong>Definitions</strong></a></p> <p><strong>Earth centered-Earth fixed Cartesian coordinate system</strong>: a Cartesian spatial reference system representing locati...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 08: Georeferencing (08 georeferencing) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md` (signal=1)
  t="_blank"><span>of Spatial Association</span></a>). If Moran&rsquo;s I indicates substantial spatial autocorrelation in the residuals, spatial statistical models should be used instead, such as various forms of spatial econometric models (Anselin, <span>1988)...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=1)
  ial reference system for accurate&nbsp;latitude, longitude, height, scale, gravity, and orientation&nbsp;throughout the United States and its territories. It provides foundational geodetic control for the nation&rsquo;s transportation, mapping, and charting&nb...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (texas_signal=1)
  ion was approximately central to the geographic area under consideration. The triangulation used to develop this datum was extended south and west to &ldquo;tie in&rdquo; to other completed surveys along the Pacific and Gulf coasts, and in 1901, this extended ...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md` (signal=45)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_VER.txt` (signal=24)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md` (signal=18)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (signal=14)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=11)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_MTL.txt` (signal=9)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats-2.html` (signal=7)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats.html` (signal=7)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-015.md` (signal=6)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=5)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_GCP.txt` (signal=5)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g3502666a4db7ba33a46f24ef7798699d/georeferencing.html` (signal=4)
