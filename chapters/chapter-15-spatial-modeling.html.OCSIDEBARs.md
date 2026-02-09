# OCSIDEBARs: chapter-15-spatial-modeling.html

Page title: Chapter 15: Spatial Modeling | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-15-spatial-modeling.html`

## Concepts (for context)
- workflow
- parameters
- reproducibility
- suitability model
- validation
- Stop &amp; check
- -  What is a Spatial Model?
- ModelBuilder: Visual Programming
- Concept: A Geoprocessing Chain
- Chapter 15 Checkpoint
- Dr. Jack Dangermond
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 15: Spatial Modeling (15 spatial modeling), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (signal=63)
  form. The resulted visual workflow is useful when the same processing steps need to be repeated on different spatial data (e.g. other areas, another period). In the case of visual programming languages, simple graphical symbols represent spatial operations imp...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-04-019.md` (signal=4)
  be learned in the <a href="https://gistbok.ucgis.org/knowledge-area/programming-and-development" target="_blank">Programming &amp; Development section</a>.</p> <p><strong>5.2 Cartographic Communication</strong></p> <p>Cartography and visualization are complex ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=1)
  ocial sensing, public health, crime analysis, surveillance and safety, just to name a few. In addition, some recent developed machine learning and particularly deep learning methods are also motivated by GIS, geography, cartography, and spatial statistics, suc...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=1)
  graphy (roughness and slope), hydrography (streams and irrigation channels, surface drainage), soils and erosion risks, proximity to population centers, and impacts on recreation, historic preservation, visual and sonic aesthetics. Data for all of these can be...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 15: Spatial Modeling (15 spatial modeling), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-038.md` (signal=222)
  e Geographic Information Science &amp; Technology Body of Knowledge. Washington, DC: Association of American Geographers.&nbsp;</p> ## Description <p>People recognize and characterize patterns to understand the world. Spatial data exhibit distinctive character...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-01-020.md` (signal=105)
  # AM-01-020 - Geospatial Analysis and Model Building Source: https://gistbok-ltb.ucgis.org/page/34/concept/10469 ## Introduction <p>Qiang, Y. (2021). Geospatial Analysis and Model Building.&nbsp;The Geographic Information Science &amp
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=62)
  udies and support automated decision making. In this knowledge entry, the fundamentals of Machine Learning (ML) are introduced, focusing on how feature spaces, models and algorithms are being developed and applied in geospatial studies. An example of a ML work...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-04-019.md` (signal=56)
  ponents are used and deployed to achieve goals.</p> <p>Effective management is necessary to meet the goals of the enterprise and deliver value that exceeds the cost to design, develop, and operate the GIS. Effective geospatial technology management assumes ong...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 15: Spatial Modeling (15 spatial modeling) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-04-019.md` (signal=8)
  may expect to formulate policies and resource allocation practices based on equity and social justice principles, but their offices and agencies will also have many ESJ-practitioners, typically trained in demographics, public health, public administration, soc...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=7)
  stem science (Reichstein et al. 2019). Table 2 summarizes some examples of ML applications with key references in land use, soil mapping and environmental susceptibility, transportation, smart cities and social sensing, public health, crime analysis, surveilla...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-010.md` (signal=7)
  nbsp;to mathematically model and understand the underlying determinants of these flows/influences.&nbsp;Proponents of SI modeling include economic geographers, regional scientists, and regional&nbsp;planners, as well as climate scientists, physicists, animal e...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=7)
  nce. Landscape architects are planners, developers and builders. As a foundation for their work, landscape architects acknowledge the prominence of nature in the human world, and design to align ecological, societal and economic factors in their designs and bu...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (texas_signal=3)
  GIS (2.0 Dufour) and Graphical Modeler for GRASS GIS; these are both open source GIS software programs.&nbsp;QGIS Processing Modeler was remade and improved in version 3.0 in 2018.&nbsp; Remote sensing software ENVI, by Harris Geospatial Solutions, introduced ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CP-05-027.md` (texas_signal=1)
  ditional data sources, they were not explicitly designed for research and rarely come packaged as tidy, organized datasets. Transforming them requires particular effort and attention to render them usable for analytics (Harris et al., 2017; Singleton and Arrib...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-028.md` (signal=44)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=31)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-02-025.md` (signal=31)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (signal=29)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CP-01-026.md` (signal=22)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-04-038.md` (signal=22)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-01-020.md` (signal=21)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CP-05-027.md` (signal=21)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-010.md` (signal=17)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-07-078.md` (signal=16)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-038.md` (signal=15)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/KE-04-019.md` (signal=14)
