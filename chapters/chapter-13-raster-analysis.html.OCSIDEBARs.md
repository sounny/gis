# OCSIDEBARs: chapter-13-raster-analysis.html

Page title: Chapter 13: Raster Spatial Analysis | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-13-raster-analysis.html`

## Concepts (for context)
- map algebra
- NoData
- resampling
- alignment
- focal/zonal operations
- Stop &amp; check
- What is Map Algebra?
- The Four Scopes
- Interactive: Local Algebra (Add)
- Chapter 13 Checkpoint
- C. Dana Tomlin
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 13: Raster Spatial Analysis (13 raster analysis), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (signal=63)
  form. The resulted visual workflow is useful when the same processing steps need to be repeated on different spatial data (e.g. other areas, another period). In the case of visual programming languages, simple graphical symbols represent spatial operations imp...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=4)
  an></p> <figure class="image"><img alt="linear streets after rasterized" height="505" src="https://bok-figures.s3.amazonaws.com/files/DM86_Fig2_combined.png" width="457" /> <figcaption>Figure 2. A linear street network symbolized via functional class specifica...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-025.md` (signal=3)
  om coarse to higher resolution data sets, and from line printers to early plotters. These same technological pathways and developments were taking place in academic settings, and this was affecting GIS (Dobson 1983) and cartography alike (Dymon 1996). Most ear...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (signal=2)
  al titles and their respective codes, as these facilitate linkages between industry, government, and academia. For example, by 2014 the Department of Homeland Security had added &ldquo;Geographic Information Science and Cartography&rdquo; to its list of sancti...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 13: Raster Spatial Analysis (13 raster analysis), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=131)
  # PD-05-033 - GDAL/OGR and Geospatial Data IO Libraries Source: https://gistbok-ltb.ucgis.org/page/34/concept/10769 ## Introduction <p>Qin, C-Z. and Zhu, L-J. (2020).&nbsp;GDAL/OGR and Geospatial Data IO Libraries.&nbsp;&nbsp;The Geographic Inform
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-04-077.md` (signal=96)
  # DM-04-077 - Spatial Joins Source: https://gistbok-ltb.ucgis.org/page/34/concept/10656 ## Introduction <p>Morgan, J. D. (2023). Spatial Joins.&nbsp;The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(1st Qu
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (signal=54)
  tes offered by colleges and universities, as well as the various professional and technical certifications that provide evidence of training and development for the workforce. Establishment of the GeoTech Center, the Geospatial Technology Competency Model, and...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=54)
  p; Technology Body of Knowledge (2024 Edition), John P. Wilson (Ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2024.1.7" target="_blank">10.22224/gistbok/2024.1.7</a></p> ## Description <p><span><span><span>Spatial data can be represented in vector ...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 13: Raster Spatial Analysis (13 raster analysis) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=7)
  nce. Landscape architects are planners, developers and builders. As a foundation for their work, landscape architects acknowledge the prominence of nature in the human world, and design to align ecological, societal and economic factors in their designs and bu...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=5)
  in querying a raster layer based on its attribute values and are always used in tandem with Boolean operators. For example, to answer the first question in Table 3 &ldquo;Which areas have high population density AND low disaster frequency?&rdquo;, we can first...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (signal=4)
  &rdquo; (Jacobs and Hawley, 2009, p. 2543).&nbsp; It provides a benefit to the individual workers through an increase in skill level, to an organization through providing a quality employee, and to society with a stable economic platform coming from a well-pai...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (texas_signal=3)
  GIS (2.0 Dufour) and Graphical Modeler for GRASS GIS; these are both open source GIS software programs.&nbsp;QGIS Processing Modeler was remade and improved in version 3.0 in 2018.&nbsp; Remote sensing software ENVI, by Harris Geospatial Solutions, introduced ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-025.md` (texas_signal=2)
  izations/gis-mapping-spatial-analysis?" target="_blank">University of Toronto</a>. Some MOOCs exist for specific audiences, such as this <a href="https://journalismcourses.org/MAP0918.html" target="_blank">University of Texas one for journalists</a>, and Esri&...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (signal=47)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=6)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-033.md` (signal=5)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-023.md` (signal=5)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (signal=4)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-04-077.md` (signal=3)
- `C:/Users/sounn/Git/gis/references/bok-mapping.md` (signal=3)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (signal=3)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=2)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=2)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-086.md` (signal=2)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-01-025.md` (signal=2)
