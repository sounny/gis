# OCSIDEBARs: chapter-04-gps.html

Page title: Chapter 4: GNSS & Positioning | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-04-gps.html`

## Concepts (for context)
- GNSS
- trilateration
- multipath
- differential correction
- datum
- Stop &amp; check
- What is GNSS?
- The Three Segments
- Accuracy Visualizer
- Interactive: Trilateration Simulator
- How Trilateration Works
- Chapter 4 Checkpoint
- Dr. Gladys West
- Greg Winfree
- Blast from the Past
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 4: GNSS & Positioning (04 gps), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-047.md` (signal=4)
  pan>5. Auxiliary Latitudes</span></span></span></span></span></span></h4> <p><span><span><span><span><span><span>Various latitude definitions are used in special applications such as astronomy, geodesy, geophysics, and cartography. Astronomic latitude </span><...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=1)
  . Values of a and b are used to compute values of f, &epsilon;2, and &epsilon;&#39;2, which, individually, can be used to describe the noncircularity of an ellipsoid. The literature often interchanges e and &epsilon; as symbols representing eccentricity. Figur...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 4: GNSS & Positioning (04 gps), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-02-030.md` (signal=114)
  # KE-02-030 - The Geospatial Industry Source: https://gistbok-ltb.ucgis.org/page/34/concept/10737 ## Introduction <p>Wilson, J. P. (2025).&nbsp;<span><span><span>The Geospatial Industry. The Geographic Information Science and Technology B
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-02-003.md` (signal=22)
  y the North American Vertical Datum of 1988 (NAVD88) can be up to 36 meters.&nbsp; Thus, it is imperative to also specify both the horizontal datum (e.g. NAD83) and the vertical datum, such as NAVD88 or the new National Spatial Reference System (NSRS) desired ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (signal=22)
  ments on a curved Earth surface, such as latitude and longitude, Cartesian coordinates are measured in consistent, standard units like meters or feet. This uniformity simplifies calculations of distance, area, and other spatial properties, making the system hi...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (signal=20)
  geopotential at a point.</p> <p><strong>GNSS</strong> &ndash; Global Navigation Satellite System. A general reference to any artificial satellite system that uses a constellation of satellites to provide autonomous geospatial positioning.</p> <p><strong>GPS</s...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 4: GNSS & Positioning (04 gps) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-02-030.md` (signal=14)
  stations, laser rangefinders, UAVs, inertial navigation systems and their software processing tools include SketchUp, which is used extensively in architecture, construction, interior design, landscape architecture, and urban planning applications. Trimble </s...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (signal=5)
  /p> <p><span><span><span>With this kind of nested precision, responders and map users can communicate the location of interest with as much or as little detail as needed. For emergency management, search-and-rescue, or disaster relief teams, USNG dramatically ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (signal=4)
  ellipsoids to report ellipsoid heights. Increasingly, gravity measurements, positional data from GNSS (Global Navigation Satellite System), and other sophisticated measurement technologies GRACE-FO (Gravity Recovery and Climate Experiment &ndash; Follow On) ar...
- `C:/Users/sounn/Git/gis/references/gpsworkshop-main/introduction.html` (signal=2)
  pping</strong> Land management, GIS, construction</li> <li><strong>Timing</strong> Financial transactions, telecommunications, power grids</li> <li><strong>Scientific Research</strong> Climate change, earthquake monitoring, atmospheric studies</li> <li><strong...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (texas_signal=3)
  while others are split between two or more (Figure 3). For instance, states like Alabama and Colorado are mostly contained within a single UTM zone which are16N and 13N respectively. However, states such as California, Texas, and New York span multiple zones d...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (texas_signal=1)
  MSL is higher than would exist on a perfectly spherical Earth surface. Source: <a href="https://www.nasa.gov/audience/foreducators/k-4/features/F_Measuring_Gravity_With_Grace.html" target="_blank">NASA and University of Texas Center for Space Research</a>.&nbs...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (texas_signal=1)
  ion was approximately central to the geographic area under consideration. The triangulation used to develop this datum was extended south and west to &ldquo;tie in&rdquo; to other completed surveys along the Pacific and Gulf coasts, and in 1901, this extended ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-044.md` (texas_signal=1)
  r the current models of the US and Canada, &ldquo;&hellip;near optimal though some small change may be required depending pending refinement of the results along the eastern coast of the U.S.A., where the effects of the Gulf Stream complicate this analysis.&rd...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-051.md` (signal=123)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-02-003.md` (signal=105)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-052.md` (signal=84)
- `C:/Users/sounn/Git/gis/references/gpsworkshop-main/how-gps-works.html` (signal=31)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/introduction-to-gps.html` (signal=29)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-048.md` (signal=28)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=26)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-044.md` (signal=24)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/introduction-to-gps.md` (signal=16)
- `C:/Users/sounn/Git/gis/references/gpsworkshop-main/introduction.html` (signal=14)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-02-030.md` (signal=13)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-05-047.md` (signal=10)
