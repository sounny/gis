# OCSIDEBARs: chapter-11-image-classification.html

Page title: Chapter 11: Image Classification | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-11-image-classification.html`

## Concepts (for context)
- training data
- validation
- classifier
- features
- confusion matrix
- overfitting
- Stop &amp; check
- The Challenge of Interpretation
- Supervised vs. Unsupervised
- Chapter 11 Checkpoint
- Alexander von Humboldt
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 11: Image Classification (11 image classification), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s13-cartographic-principles.html` (signal=109)
  rom GIS tools and toward cartographic tools, although the two are becoming more and more inextricably bound. Unfortunately, many GIS users are never exposed to the field of <span class="margin_term"><a class="glossterm">cartography</a><span class="glossdef">Th...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-06-021.md` (signal=39)
  hands, that people use to make decisions. This encompassing view of maps allows the inclusion of a variety of &nbsp;map forms that are otherwise awkward to categorize, such as mental maps (see&nbsp;<strong>Participatory Cartography,&nbsp;</strong>forthcoming),...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=9)
  s of any and all geographic information systems (GISs). For instance, maps constitute both the input and output of a GIS. Hence a GIS utilizes many concepts and themes from <span class="margin_term"><a class="glossterm">cartography</a><span class="glossdef">Th...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-085.md` (signal=7)
  i> <li>Generalization Techniques for Point, Line, and Area Data</li> <li>Generalization Challenges, Evaluation, and Research Outlook</li> </ol> <p>&nbsp;</p> <p><a><strong>1. Definitions</strong></a></p> <p><strong>Cartography</strong>: Process of designing, m...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 11: Image Classification (11 image classification), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-06-013.md` (signal=121)
  # FC-06-013 - Spatial Queries Source: https://gistbok-ltb.ucgis.org/page/34/concept/10701 ## Introduction <p>Yao, X. (2021). Spatial Queries.&nbsp;The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(1st Quar
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=79)
  # DC-01-042 - Changes in Geospatial Data Capture Over Time: Part 2, Implications and Case Studies Source: https://gistbok-ltb.ucgis.org/page/34/concept/10620 ## Introduction <p>Cowen, D. J. and Anderson, K. E. (2021).&nbsp;Changes in Geospatial
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s10-data-characteristics-and-visua.html` (signal=64)
  ub.css" rel="stylesheet" type="text/css"> <title>Data Characteristics and Visualization</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s09-geospatial-data-management.html"><img src="shared/images/batch-left.pn...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=62)
  udies and support automated decision making. In this knowledge entry, the fundamentals of Machine Learning (ML) are introduced, focusing on how feature spaces, models and algorithms are being developed and applied in geospatial studies. An example of a ML work...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 11: Image Classification (11 image classification) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=9)
  DLG files provided a useful multi-layer base map for numerous applications across the United States. For example, in South Carolina, the Department of Commerce used the 1:100,000 DLG to create a major statewide GIS for economic development. Additional layers s...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=7)
  y contain thematic information. What is more, when used in conjunction, thematic and reference maps often complement each other.</p> <p class="para editable block" id="campbell_1.0-ch02_s01_s02_p03">For example, public health officials in a city may be interes...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=7)
  stem science (Reichstein et al. 2019). Table 2 summarizes some examples of ML applications with key references in land use, soil mapping and environmental susceptibility, transportation, smart cities and social sensing, public health, crime analysis, surveilla...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-071.md` (signal=7)
  pes of data) available to the public as Volunteered Geographic Information (VGI) (Goodchild, 2007). A transportation planner often needs to combine all sorts of information about transportation infrastructure and social-economic characteristics of the populati...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-066.md` (texas_signal=1)
  into a common river is typically referred to as a drainage basin. A drainage basin can be composed of thousands of smaller watersheds.&nbsp; The Mississippi River Basin flows to the mouth of the Mississippi River at the Gulf of Mexico (Figure 2). It encompasse...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-066.md` (signal=56)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s06-map-anatomy.html` (signal=52)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s10-data-characteristics-and-visua.html` (signal=50)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s10-02-searches-and-queries.html` (signal=48)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-06-021.md` (signal=48)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-085.md` (signal=47)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-071.md` (signal=44)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-08-094.md` (signal=42)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-06-013.md` (signal=42)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s13-cartographic-principles.html` (signal=39)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=36)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=36)
