# OCSIDEBARs: chapter-05-analysis.html

Page title: Chapter 05: Spatial Analysis | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-05-analysis.html`

## Concepts (for context)
- Buffer
- Intersect
- Union
- Map Algebra
- Euclidean Distance
- Boolean Logic
- The Analysis Workflow
- 1. Selection & Query
- 2. Vector Overlay Analysis
- 3. Raster Map Algebra
- Interactive: Suitability Studio
- 4. Neighborhoods & Proximity
- Buffering
- Interpolation
- Theissen Polygons
- Ian McHarg
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 05: Spatial Analysis (05 analysis), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=4)
  an></p> <figure class="image"><img alt="linear streets after rasterized" height="505" src="https://bok-figures.s3.amazonaws.com/files/DM86_Fig2_combined.png" width="457" /> <figcaption>Figure 2. A linear street network symbolized via functional class specifica...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-067.md` (signal=2)
  the resultant interpolation. The method is covered in greater detail in this Body of Knowledge entry.</li> </ul> <p>&nbsp;</p> <h4>3. Contouring</h4> <p>One way to represent a 3-dimensional surface with 2-dimensional symbols is by contours. These are lines of ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-017.md` (signal=1)
  quo;) is a declarative programming language that is closely linked to E.F. Codd&rsquo;s relational database model (Codd 1970). Its English-like syntax was designed at the outset to provide a more accessible way than the symbolic logic then in use to create the...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 05: Spatial Analysis (05 analysis), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=54)
  p; Technology Body of Knowledge (2024 Edition), John P. Wilson (Ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2024.1.7" target="_blank">10.22224/gistbok/2024.1.7</a></p> ## Description <p><span><span><span>Spatial data can be represented in vector ...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=43)
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Geospatial Analysis I: Vector Operations</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a h...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-017.md` (signal=41)
  ta structures (tables) and other database objects. Important additions to the SQL standard include SQL/PSM, which adds control flow, local variables, and other procedural language features; and SQL/MM Part 3, which adds spatial support. Many complex geoprocess...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-040.md` (signal=40)
  022 Edition), John P. Wilson (Ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2022.2.2" target="_blank">10.22224/gistbok/2022.2.2</a>.</p> ## Description <p>Areal interpolation is the process of transforming spatial data from source zones with known ...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 05: Spatial Analysis (05 analysis) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=5)
  in querying a raster layer based on its attribute values and are always used in tandem with Boolean operators. For example, to answer the first question in Table 3 &ldquo;Which areas have high population density AND low disaster frequency?&rdquo;, we can first...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-042.md` (signal=3)
  s are commonly used to model migration of people between cities (Foot &amp; Milne, 1984; Karemera, Oguledo, &amp; Davis, 2000; Plane, 1984). In such a model, the flow of people is dependent on the mass (e.g. population, economic opportunity) of the city and th...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-071.md` (signal=2)
  ). Numerical solution enables incorporation of stream enforcement and other topographic features (Hutchinson 1989) with the computational cost proportional to the number of interpolated grid points. To interpolate large climate data sets, Hancock and Hutchinso...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=2)
  ch land parcels are for sale and which are zoned for commercial development. After collecting and overlaying the baseline information on available development zones, you can begin to determine which areas offer the most economic opportunity by collecting regio...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-027.md` (texas_signal=23)
  e basis for many of the tools and techniques of spatial analysis (O&rsquo;Sullivan and Unwin 2003, 35-49). </span></span></span></p> <p><span><span><span>As a random example, perhaps we want to describe Tarrant County, Texas. Among its potentially useful chara...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-007.md` (texas_signal=13)
  ean center is.</p> <p>&nbsp;</p> <p><img alt="" height="627" src="https://bok-figures.s3.amazonaws.com/files/AM07_Fig1.png" width="800" /></p> <p>Figure 1: The mean center and media center of fire stations in Austin, Texas. Note that some fire stations are in ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-04-019.md` (texas_signal=10)
  objects, i.e., nodes and links, physically exist in&nbsp;geographical space. In a physical network, each node is connected to a small number of spatially proximal nodes. A map of the physical network of highways in the Dallas-Fort Worth (DFW) area shows how no...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-01-027.md` (texas_signal=7)
  e of the founders of Surrealism (Wood, 2010a). The Surrealists purposely distorted the map, offering a political message against an imperialist and Eurocentric conventional representation of the world. Source:&nbsp;Beth Harris, &quot;Le monde au temps des Surr...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=79)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-040.md` (signal=75)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-01-single-layer-analysis.html` (signal=65)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (signal=51)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-067.md` (signal=45)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-003.md` (signal=43)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=41)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-071.md` (signal=35)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-017.md` (signal=32)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s12-geospatial-analysis-ii-raster-.html` (signal=27)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=25)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-042.md` (signal=25)
