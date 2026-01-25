# OCSIDEBARs: chapter-03-projections.html

Page title: Chapter 03: Geodesy & Projections | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-03-projections.html`

## Concepts (for context)
- datum
- projection
- EPSG
- Web Mercator
- distortion
- Stop &amp; check
- The Fundamental Geodetic Challenge
- Latitude, Longitude & The Graticule
- Interactive Projection Explorer
- Projection Surfaces
- The "Big Four" Distortions
- Map Preprocessing
- 1. Georeferencing
- 2. Resampling
- 3. Edge Matching
- State Plane Coordinate System (SPCS)
- Chapter 03 Checkpoint
- Eratosthenes
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 03: Geodesy & Projections (03 projections), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-06-021.md` (signal=39)
  hands, that people use to make decisions. This encompassing view of maps allows the inclusion of a variety of &nbsp;map forms that are otherwise awkward to categorize, such as mental maps (see&nbsp;<strong>Participatory Cartography,&nbsp;</strong>forthcoming),...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-03-006.md` (signal=12)
  te presenting key properties, characteristics, and preferred uses of many historically important projections and of those frequently used by mapmakers today.</li> <li>Adaptive Composite Map Projections (<a href="http://cartography.oregonstate.edu/demos/Adaptiv...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=9)
  s of any and all geographic information systems (GISs). For instance, maps constitute both the input and output of a GIS. Hence a GIS utilizes many concepts and themes from <span class="margin_term"><a class="glossterm">cartography</a><span class="glossdef">Th...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=1)
  . Values of a and b are used to compute values of f, &epsilon;2, and &epsilon;&#39;2, which, individually, can be used to describe the noncircularity of an ellipsoid. The literature often interchanges e and &epsilon; as symbols representing eccentricity. Figur...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 03: Geodesy & Projections (03 projections), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-03-006.md` (signal=26)
  nates. All map projections introduce distortion (e.g., to areas, angles, distances) in the resulting planar coordinates. Understanding what, where, and how much distortion is introduced is an important consideration for spatial computations and visual interpre...
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab5/cntpop_2004.fgdc.htm` (signal=23)
  OJECTED POPULATIONS OF FLORIDA COUNTIES</h1> Metadata also available as<p> <h2>Metadata:</h2> <ul> <li><A HREF="#1">Identification_Information</A></li> <li><A HREF="#2">Data_Quality_Information</A></li> <li><A HREF="#3">Spatial_Data_Organization_Information</A...
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab6/cntpop_2004.fgdc.htm` (signal=23)
  OJECTED POPULATIONS OF FLORIDA COUNTIES</h1> Metadata also available as<p> <h2>Metadata:</h2> <ul> <li><A HREF="#1">Identification_Information</A></li> <li><A HREF="#2">Data_Quality_Information</A></li> <li><A HREF="#3">Spatial_Data_Organization_Information</A...
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab7/cntpop_2004.fgdc.htm` (signal=23)
  OJECTED POPULATIONS OF FLORIDA COUNTIES</h1> Metadata also available as<p> <h2>Metadata:</h2> <ul> <li><A HREF="#1">Identification_Information</A></li> <li><A HREF="#2">Data_Quality_Information</A></li> <li><A HREF="#3">Spatial_Data_Organization_Information</A...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 03: Geodesy & Projections (03 projections) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab5/cntpop_2004.fgdc.htm` (signal=18)
  a.dc href="http://purl.org/metadata/dublin_core"> <meta name="dc.title" content="HISTORIC AND PROJECTED POPULATIONS OF FLORIDA COUNTIES "> <meta name="dc.creator" content="University of Florida GeoPlan Center, Bureau of Economic and Business Research, and US C...
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab6/cntpop_2004.fgdc.htm` (signal=18)
  a.dc href="http://purl.org/metadata/dublin_core"> <meta name="dc.title" content="HISTORIC AND PROJECTED POPULATIONS OF FLORIDA COUNTIES "> <meta name="dc.creator" content="University of Florida GeoPlan Center, Bureau of Economic and Business Research, and US C...
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab7/cntpop_2004.fgdc.htm` (signal=18)
  a.dc href="http://purl.org/metadata/dublin_core"> <meta name="dc.title" content="HISTORIC AND PROJECTED POPULATIONS OF FLORIDA COUNTIES "> <meta name="dc.creator" content="University of Florida GeoPlan Center, Bureau of Economic and Business Research, and US C...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=7)
  y contain thematic information. What is more, when used in conjunction, thematic and reference maps often complement each other.</p> <p class="para editable block" id="campbell_1.0-ch02_s01_s02_p03">For example, public health officials in a city may be interes...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (texas_signal=3)
  while others are split between two or more (Figure 3). For instance, states like Alabama and Colorado are mostly contained within a single UTM zone which are16N and 13N respectively. However, states such as California, Texas, and New York span multiple zones d...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (texas_signal=1)
  MSL is higher than would exist on a perfectly spherical Earth surface. Source: <a href="https://www.nasa.gov/audience/foreducators/k-4/features/F_Measuring_Gravity_With_Grace.html" target="_blank">NASA and University of Texas Center for Space Research</a>.&nbs...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (texas_signal=1)
  ion was approximately central to the geographic area under consideration. The triangulation used to develop this datum was extended south and west to &ldquo;tie in&rdquo; to other completed surveys along the Pacific and Gulf coasts, and in 1901, this extended ...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-03-006.md` (signal=151)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (signal=88)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (signal=87)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=84)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-02-map-scale-coordinate-systems-a.html` (signal=80)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=80)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=67)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-06-021.md` (signal=47)
- `C:/Users/sounn/Git/gis/references/gpsworkshop-main/eratosthenes.html` (signal=36)
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab5/cntpop_2004.fgdc.htm` (signal=25)
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab6/cntpop_2004.fgdc.htm` (signal=25)
- `C:/Users/sounn/Git/gis/references/MapsAndGraphs/labdata/Lab7/cntpop_2004.fgdc.htm` (signal=25)
