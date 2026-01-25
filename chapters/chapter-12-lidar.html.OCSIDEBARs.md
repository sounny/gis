# OCSIDEBARs: chapter-12-lidar.html

Page title: Chapter 12: LiDAR & 3D Analysis | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-12-lidar.html`

## Concepts (for context)
- LiDAR
- point cloud
- return
- intensity
- nDSM/CHM
- Stop &amp; check
- What is LiDAR?
- Pulse Interaction
- DEM, DSM, and CHM
- Chapter 12 Checkpoint
- Martin Isenburg
- Texas Connection

## Sidebar: GIS Is an Art

GIS is an art because it turns messy reality into a deliberate visual argument. Every dataset is a material (pixels, points, lines), and every map is a composition that directs attention, reveals pattern, and makes a claim about what matters. In this chapter on Chapter 12: LiDAR & 3D Analysis (12 lidar), treat the workflow like studio practice: iterate, compare alternatives, and explain your design choices (not just the button clicks).

Prompts:
- Studio move: make two versions of the same map/output (clean vs expressive) and write 3 sentences on what story each tells.
- Constraint exercise: limit yourself to 2 colors + 1 accent; what becomes clearer? what becomes hidden?
- Craft check: name one choice you made for clarity (legibility) and one choice you made for feeling (mood).

Reference seeds:
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/ge6b3417ef3826def228c06afbaac1d8a/spectral-indices.html` (signal=4)
  age.png" data-api-endpoint="https://ufl.instructure.com/api/v1/courses/541369/files/100381389" data-api-returntype="File" loading="lazy"></strong></em></p> <p>7- Right-click the NDVI layer in the Contents pane and go to Symbology. Choose a color scheme (I pick...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g840cdc38eeb40da60f583c3d4985d9df/spatial-point-pattern-analysis.html` (signal=4)
  1369/files/99926629" data-api-returntype="File" loading="lazy"></p> <p><span>17. </span><span>Unselect the point layer, then right-click on the </span><strong>Thiessen_2023</strong><span> layer and choose </span><strong>Symbology</strong><span>.</span><br><spa...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gef752b88f00be9b4059fb13a54b98713/digitizing.html` (signal=4)
  d0cb8aa7.png" alt="image.png" data-api-endpoint="https://ufl.instructure.com/api/v1/courses/541369/files/100149708" data-api-returntype="File" loading="lazy"></span></p> <ol start="15"> <li class="text-start">Adjust the symbology for the <strong>Lines</strong>...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gce4e1157e0cc6e1e44710f163e4fc926/canopy-height-modeling-of-neon-lidar.html` (signal=3)
  xplore the 3D view by holding down the mouse scroll wheel and moving your mouse. This is LiDAR point cloud data, where each point represents a location with X, Y, and Z (elevation) values.</span></p> <p><span>3- Set the symbology by right-clicking the LiDAR la...

## Sidebar: Asking Questions of Where

Before tools, start with the question of where. 'Where' is not only a location; it is a relationship: near/far, inside/outside, connected/disconnected, changing/stable. For Chapter 12: LiDAR & 3D Analysis (12 lidar), the best work comes from translating a curiosity into a spatial test you can run and explain.

Prompts:
- Where is it concentrated, and compared to what baseline?
- Where does it change sharply (boundaries) vs gradually (surfaces)?
- Where is the data missing, biased, or uncertain?
- Where would you stand on the ground to verify it (a field check plan)?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=79)
  # DC-01-042 - Changes in Geospatial Data Capture Over Time: Part 2, Implications and Case Studies Source: https://gistbok-ltb.ucgis.org/page/34/concept/10620 ## Introduction <p>Cowen, D. J. and Anderson, K. E. (2021).&nbsp;Changes in Geospatial
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g840cdc38eeb40da60f583c3d4985d9df/spatial-point-pattern-analysis.html` (signal=20)
  <html> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <title>Assignment: Spatial Point Pattern Analysis</title> </head> <body> <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Spatial Point Pattern Analysis</st...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/ge6b3417ef3826def228c06afbaac1d8a/spectral-indices.html` (signal=5)
  lculated by taking the difference between the near-infrared (NIR) and red bands from satellite imagery, then dividing this difference by the sum of those two bands.</span></p> <p><span>NDVI values fall between -1 and 1, where low values typically represent non...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-04-038.md` (signal=4)
  ngle technique but rather a workflow exploiting multiple algorithms originally developed in computer vision and stereo photogrammetry. The SfM techniques along with multi-view stereo (MVS) algorithms can lead to a hyper-spatial resolution sampling of the real-...

## Sidebar: Interdisciplinary Thinking

GIS becomes powerful when it borrows methods and questions from other fields. A single layer is rarely the point; the point is how a spatial pattern intersects with people, policy, environmental processes, and technology. Use Chapter 12: LiDAR & 3D Analysis (12 lidar) as a bridge: pick a second discipline and ask what it would consider 'evidence' in your map.

Prompts:
- Public health: what exposure or access pattern is visible (or invisible) at your chosen scale?
- Urban planning: what zoning/transport constraint changes the interpretation of your result?
- Ecology/climate: what seasonal or physical process could explain the pattern?
- Economics: who pays, who benefits, and what is the spatial footprint of that tradeoff?

Reference seeds:
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=9)
  DLG files provided a useful multi-layer base map for numerous applications across the United States. For example, in South Carolina, the Department of Commerce used the 1:100,000 DLG to create a major statewide GIS for economic development. Additional layers s...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-099.md` (signal=3)
  ade LiDAR data collection easier and more cost-effective. With the widespread availability of LiDAR data, point cloud analysis is facilitated by various software tools and is applied in many different domains, including urban planning, forestry inventory, biom...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gce4e1157e0cc6e1e44710f163e4fc926/canopy-height-modeling-of-neon-lidar.html` (signal=2)
  al Ecological Observatory Network, is a project that collects long-term ecological data from different environments across the United States, including Alaska, Hawaii, and Puerto Rico. NEON has 81 field sites in various climate regions. Scientists use NEON dat...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gb658d2b9e8dc4aed61297c80f0b9eba8/hospital-accessibility-analysis-in-wyoming.html` (signal=2)
  <p data-pm-slice="1 1 []"><em><strong>Objectives and Introduction</strong></em></p> <p><span>Access to quality health care is essential for community wellbeing, especially in rural areas. Many factorsincluding social, economic, physical, and policy environment...

## Texas anchor candidates (Local to Global fuel)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g883c68f51edfd8cc23a659c01cc2ab36/alaska-vs-texas-does-projection-matter-when-measure-size-of-state.html` (texas_signal=12)
  <html> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <title>Assignment: Alaska vs Texas - Does Projection Matter when measure size of state?</title> </head> <body> <h1 style="text-align: center;"><span style="font-size: 14pt;"><st...

## Top supporting sources (overall signal)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-099.md` (signal=80)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-03-027.md` (signal=56)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gce4e1157e0cc6e1e44710f163e4fc926/canopy-height-modeling-of-neon-lidar.html` (signal=50)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/ge6b3417ef3826def228c06afbaac1d8a/spectral-indices.html` (signal=38)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g840cdc38eeb40da60f583c3d4985d9df/spatial-point-pattern-analysis.html` (signal=32)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-04-038.md` (signal=26)
- `C:/Users/sounn/Git/gis/references/BadMaps/WallStreetMap.html` (signal=23)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gef752b88f00be9b4059fb13a54b98713/digitizing.html` (signal=23)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-042.md` (signal=21)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g5e028da2a3fb64c0146667c28b917d35/land-cover-change-detection.html` (signal=20)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/gb658d2b9e8dc4aed61297c80f0b9eba8/hospital-accessibility-analysis-in-wyoming.html` (signal=19)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g883c68f51edfd8cc23a659c01cc2ab36/alaska-vs-texas-does-projection-matter-when-measure-size-of-state.html` (signal=18)
