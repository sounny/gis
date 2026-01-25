# OCNOTES: chapter-08-georeferencing.html

Page title: Chapter 08: Georeferencing | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-08-georeferencing.html`

## Concepts found on page
- ground control point (GCP)
- checkpoint
- residual
- RMSE
- affine transformation
- resampling
- world file
- Residual
- RMS Error (Root Mean Square)
- Affine Transformation
- Georeferencing
- What is Georeferencing?
- Ground Control Points (GCPs)
- Simulated Alignment
- Measuring Error: RMS
- Dr. Peter H. Dana

## Strongest reference sources (overall)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md` (signal=90)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (signal=47)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_VER.txt` (signal=43)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md` (signal=36)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/g3502666a4db7ba33a46f24ef7798699d/georeferencing.html` (signal=16)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (signal=16)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-02-036.md` (signal=13)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_GCP.txt` (signal=10)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DA-031.md` (signal=10)
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_MTL.txt` (signal=8)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats-2.html` (signal=7)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats.html` (signal=7)

## Candidate excerpts to adapt (verbatim seeds; paraphrase into the chapter)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md`
  # AM-04-073 - Polynomial Functions Source: https://gistbok-ltb.ucgis.org/page/34/concept/10837 ## Introduction <p>Gimond, M. (2025). Polynomial Functions. The Geographic Information Science &amp; Technology Body of Knowledge (2025 Edition), John P. Wilson (ed). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2025.1.10" target="_blank">10.22224/gistbok/2025.1.10</a></p> ## Description <p><span><span>Polynomial fun...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md`
  # DC-01-030 - Georeferencing and Georectification Source: https://gistbok-ltb.ucgis.org/page/34/concept/10616 ## Introduction <p>Lippitt, C. D. (2020). Georeferencing and Georectification.&nbsp;The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Quarter 2020 Edition), John P. Wilson (Ed.). DOI:<a href="https://doi.org/10.22224/gistbok/2020.3.3" target="_blank">10.22224/gistbok/2020.3.3</a>...
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_VER.txt`
  ============================================================================== ============================================================================== Mon. Mar. 3 2014 LANDSAT 5 Time: 14:48 Image Assessment System GEOMETRIC VERIFY Report ============================================================================== Order ID: 0101402278779_00036 Path / Row - 40 / 36 Reference Image: L51PAC1011201170100_HDF.L1G ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-063.md`
  # AM-03-063 - Regression Fundamentals Source: https://gistbok-ltb.ucgis.org/page/34/concept/10831 ## Introduction <p>Li, Z. (2024). Regression Fundamentals.&nbsp;The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(2024 Edition). John P. Wilson (ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2024.1.11" target="_blank">10.22224/gistbok/2024.1.11</a>.</p> ## Description <p>Regression a...

## Reference matches by concept (top hits)

### checkpoint
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-015.md` (matches=5)
  Excerpt: he challenge of keeping their code up-to-date with new releases and new and updated packages, though there are strategies to mitigate this, for example the <a href="https://CRAN.R-project.org/package=checkpoint" target="_blank">checkpoint package</a> by Micros...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CP-05-031.md` (matches=1)
  Excerpt: ansformations, rather than treating each step in isolation. Spark avoids unnecessary disk I/O by keeping intermediate data in memory whenever possible, and it only writes to disk for fault tolerance (checkpointing) or if data does not fit in main memory. The r...

### residual
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md` (matches=45)
  Excerpt: mensional space. This may serve many purposes including (1) describing overall changes in a variable as a function of location, (2) removing global trend from the data for the purpose of exposing the residuals (a crucial step when exploring spatial autocorrela...
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_VER.txt` (matches=19)
  Excerpt: ======= Order ID: 0101402278779_00036 Path / Row - 40 / 36 Reference Image: L51PAC1011201170100_HDF.L1G Color mapping per rank ---------------------- Rank 1 is Green: total residual <= 0.5 Rank 2 is Cyan: 0.5 < total residual <= 1 Rank 3 is Blue: 1 < total res...

### RMSE
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_MTL.txt` (matches=8)
  Excerpt: UCT_METADATA GROUP = IMAGE_ATTRIBUTES CLOUD_COVER = 0.00 IMAGE_QUALITY = 9 SUN_AZIMUTH = 115.16536546 SUN_ELEVATION = 63.48940640 GROUND_CONTROL_POINTS_MODEL = 175 GEOMETRIC_RMSE_MODEL = 3.662 GEOMETRIC_RMSE_MODEL_Y = 2.622 GEOMETRIC_RMSE_MODEL_X = 2.556 GROUN...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (matches=5)
  Excerpt: number of points recommended is at least twice this number because only GCPs beyond this minimum number allow for evaluation of model fit, which is typically measured by the root mean squared error (RMSE) between known (i.e., input at GCPs) locations and the l...

### affine transformation
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (matches=5)
  Excerpt: ></a></p> <p><strong>4.1 Plane Transformation</strong></p> <p>The coordinates of geographic features on a planar surface can be transformed using multiple methods such as similarity transformation, affine transformation, and non-linear transformations. The sim...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-071.md` (matches=1)
  Excerpt: as &ldquo;anchors&rdquo; to link two datasets, in such a way that each triangular region between the anchor points should have similar spatial displacement. The rubber-sheeting method then applies an affine transformation in each region to remove the spatial d...

### resampling
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (matches=6)
  Excerpt: without the need for manual coordinate transformations by users. The coordinate transformation mechanisms for vector and raster datasets are different because the raster datasets require pixel value resampling during coordinate transformations. As a case study...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (matches=4)
  Excerpt: squared error (RMSE) between known (i.e., input at GCPs) locations and the locations estimated by the model.</p> <p>The three orders of polynomial warping are often conflated with a related process, resampling. Georeferencing processes simply estimate the loca...

### world file
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats-2.html` (matches=7)
  Excerpt: n. JPEG 2000 is a non-proprietary image compression format based on ISO standards, and typically uses .jp2 as the file extension. Its advantages are that it offers lossy and lossless compression, and world files (.j2w) can be used to georeference an image in G...
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/popular-raster-data-formats.html` (matches=7)
  Excerpt: n. JPEG 2000 is a non-proprietary image compression format based on ISO standards, and typically uses .jp2 as the file extension. Its advantages are that it offers lossy and lossless compression, and world files (.j2w) can be used to georeference an image in G...

### Residual
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-073.md` (matches=45)
  Excerpt: mensional space. This may serve many purposes including (1) describing overall changes in a variable as a function of location, (2) removing global trend from the data for the purpose of exposing the residuals (a crucial step when exploring spatial autocorrela...
- `C:/Users/sounn/Git/gis/references/Assignments/Classification/SupervisedClassification/LandSatImage/LT50400362011201PAC01_VER.txt` (matches=19)
  Excerpt: ======= Order ID: 0101402278779_00036 Path / Row - 40 / 36 Reference Image: L51PAC1011201170100_HDF.L1G Color mapping per rank ---------------------- Rank 1 is Green: total residual <= 0.5 Rank 2 is Cyan: 0.5 < total residual <= 1 Rank 3 is Blue: 1 < total res...

### Affine Transformation
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-06-088.md` (matches=5)
  Excerpt: ></a></p> <p><strong>4.1 Plane Transformation</strong></p> <p>The coordinates of geographic features on a planar surface can be transformed using multiple methods such as similarity transformation, affine transformation, and non-linear transformations. The sim...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-071.md` (matches=1)
  Excerpt: as &ldquo;anchors&rdquo; to link two datasets, in such a way that each triangular region between the anchor points should have similar spatial displacement. The rubber-sheeting method then applies an affine transformation in each region to remove the spatial d...

### Georeferencing
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-01-030.md` (matches=28)
  Excerpt: # DC-01-030 - Georeferencing and Georectification Source: https://gistbok-ltb.ucgis.org/page/34/concept/10616 ## Introduction <p>Lippitt, C. D. (2020). Georeferencing and Georectification.&nbsp;The Geographic Information Science &amp; Technology Body of Knowle...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-02-036.md` (matches=13)
  Excerpt: n interpretation of historical maps, and some example applications.</p> ## Explanation <ol> <li>Introduction</li> <li>Acquisition of Historical Maps</li> <li>Symbols and Interpretation</li> <li>Georeferencing&nbsp;an Historical Map</li> <li>Digitization of His...

### Ground Control Points (GCPs)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-03-024.md` (matches=1)
  Excerpt: ude: (1) direct, which uses known camera locations through GNSS-enabled cameras or onboard GNSS and IMU measurements stored and attached&nbsp;to captured images, (2) indirect, which uses GNSS-located ground control points (GCPs), and (3) a combination of direc...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DC-04-038.md` (matches=1)
  Excerpt: ntation is usually solved efficiently via bundle adjustment (Starek and Wilkinson, 2022). An alternative approach to constrain the SfM-MVS solution can be through introducing an appropriate number of ground control points (GCPs) to the SfM-MVS procedure. GCP c...

## Proposed adaptation to the book (concrete next edits for another agent)
- Interactive module candidates:
  - Georeferencing game: drag GCPs onto matching features; live RMS error readout; show how bad points warp the map.
- Local-to-Global sidebar: search within the listed reference sources for a Texas anchor (Houston, Galveston, Austin, DFW, Rio Grande, Permian Basin) and write a 120-180 word sidebar that ends with a global parallel.
- 'Important Persons' bio box: if any reference source includes an inventor/author tied to this topic, add a 1-paragraph bio + 3 bullets (impact, algorithm/idea, modern use).
- Critical GIS prompt: add 1 dilemma question connected to the chapter's primary dataset choice (scale, privacy, bias, uncertainty) and ask for a written justification.
