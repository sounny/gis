# OCNOTES: chapter-05-analysis.html

Page title: Chapter 05: Spatial Analysis | GIS Digital Textbook

Source page: `C:/Users/sounn/Git/gis/chapters/chapter-05-analysis.html`

## Concepts found on page

- Buffer
- Intersect
- Union
- Map Algebra
- Euclidean Distance
- Boolean Logic
- Spatial Analysis
- Learning Outcomes
- Key Terms
- The Analysis Workflow
- 1. Selection & Query
- 2. Vector Overlay Analysis
- 3. Raster Map Algebra
- 4. Neighborhoods & Proximity
- Buffering
- Interpolation
- Theissen Polygons
- Ian McHarg

## Strongest reference sources (overall)

- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (signal=70)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-040.md` (signal=68)
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-01-single-layer-analysis.html` (signal=63)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (signal=50)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-067.md` (signal=45)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-003.md` (signal=43)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (signal=39)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-071.md` (signal=35)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-042.md` (signal=22)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/module-12-spatial-interpolation-2.html` (signal=22)
- `C:/Users/sounn/Git/gis/references/uf_canvas_extract/wiki_content/module-12-spatial-interpolation.html` (signal=22)
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-01-028.md` (signal=21)

## Candidate excerpts to adapt (verbatim seeds; paraphrase into the chapter)

- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html`
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Geospatial Analysis I: Vector Operations</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s10-data-characteristics-and-visua.html"><img src="shared/images/batch-left.png"></a> <a href="s10-data-characteristics-and-visua.html">Previous Chapter</a...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-040.md`
  # AM-02-040 - Areal Interpolation Source: https://gistbok-ltb.ucgis.org/page/34/concept/10479 ## Introduction <p>Comber, A. and Zeng, W. (2022). Areal Interpolation. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(2nd Quarter 2022 Edition), John P. Wilson (Ed.). DOI:&nbsp;<a href="https://doi.org/10.22224/gistbok/2022.2.2" target="_blank">10.22224/gistbok/2022.2.2</a>.</p> ## Description <...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-01-single-layer-analysis.html`
  <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <link href="shared/bookhub.css" rel="stylesheet" type="text/css"> <title>Single Layer Analysis</title> </head> <body> <div id=navbar-top class="navbar"> <div class="navbar-part left"> <a href="s10-03-data-classification.html"><img src="shared/images/batch-left.png"></a> <a href="s10-03-data-classification.html">Previous Section</a> </div> <div class="navbar-part mi...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md`
  # AM-02-006 - Grid Operations and Map Algebra Source: https://gistbok-ltb.ucgis.org/page/34/concept/10457 ## Introduction <p>Mennis, J. (2022). Grid Operations and Map Algebra. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Quarter 2022 Edition). John P. Wilson (Ed.).&nbsp; DOI:<a href="https://doi.org/10.22224/gistbok/2022.3.1" target="_blank">10.22224/gistbok/2022.3.1</a></p> <p>Thi...

## Reference matches by concept (top hits)

### Buffer

- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (matches=59)
  Excerpt: itable block" id="campbell_1.0-ch07_s01_p01">As the name suggests, single layer analyses are those that are undertaken on an individual feature dataset. <span class="margin_term"><a class="glossterm">Buffering</a><span class="glossdef">Placing a region of spec...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-01-single-layer-analysis.html` (matches=58)
  Excerpt: itable block" id="campbell_1.0-ch07_s01_p01">As the name suggests, single layer analyses are those that are undertaken on an individual feature dataset. <span class="margin_term"><a class="glossterm">Buffering</a><span class="glossdef">Placing a region of spec...

### Intersect

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (matches=23)
  Excerpt: ally aligned precisely with each other to ensure a correct overlay operation. In general, vector overlay is geometrically and computationally complex. Some most used vector overlay operations include intersection, union, erase, and clip. Raster overlay combine...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-01-028.md` (matches=16)
  Excerpt: context of applications. In spatial databases, adopting the vector data model of the Open Geospatial Consortium, topological relationships are evaluated either on the base of the Dimension-Extended 9-Intersection Model (DE9-IM) or the so-called Named Topologic...

### Union

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (matches=14)
  Excerpt: recisely with each other to ensure a correct overlay operation. In general, vector overlay is geometrically and computationally complex. Some most used vector overlay operations include intersection, union, erase, and clip. Raster overlay combines multiple ras...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-03-018.md` (matches=11)
  Excerpt: td> </tr> <tr> <td>MPI Operator</td> <td>Explanation</td> </tr> <tr> <td> <p>MPI_POINT</p> <p>MPI_LINE</p> MPI_RECT</td> <td> <p>MPI_MIN</p> <p>MPI_MAX</p> MPI_UNION</td> <td> <p>Min point (bottom left corner)</p> <p>Max point (top right corner)</p> MBR of Geo...

### Map Algebra

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-006.md` (matches=47)
  Excerpt: # AM-02-006 - Grid Operations and Map Algebra Source: https://gistbok-ltb.ucgis.org/page/34/concept/10457 ## Introduction <p>Mennis, J. (2022). Grid Operations and Map Algebra. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(3rd Qua...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-004.md` (matches=2)
  Excerpt: logical operations with binary variables (true or false). Boolean algebra uses the logical operators (AND, OR, NOT, XOR), to determine whether a particular condition is true or false.</p> <p><strong>Map algebra: </strong>a framework to analyze gridded data val...

### Euclidean Distance

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/FC-05-042.md` (matches=10)
  Excerpt: t of the distance operations, several methods of measuring distance may be used. The choice of the distance measure used may significantly alter the results of the operation.</p> <p><strong>2.1&nbsp;Euclidean Distance</strong></p> <p>Euclidean Distance is the ...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-009.md` (matches=4)
  Excerpt: p>Spatial clustering may include non-spatial attributes or variables. Non-spatial clustering will rely entirely on attributes of the observed data, but use ideas already familiar to GIS users such as Euclidean distances (see below). Clustering is seen in many ...

### Boolean Logic

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-09-088.md` (matches=12)
  Excerpt: ship, with anything between 0 and 1 being a partial belonging. The &ldquo;around 2 p.m.&rdquo; above is the result under fuzzy logic. By the same token, there is an aggregation that is done under the Boolean logic which only admits belonging (1) or not belongi...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DM-02-020.md` (matches=2)
  Excerpt: <p>Figure 1. Hierarchy of mathematical spaces increasing specialization and adding constraints. Source: author.</p> <p>&nbsp;</p> <p>At the lowest (most abstract) level, we have logic. We will use Boolean logic with its NOT, AND, and OR operators as a stand-in...

### Spatial Analysis

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-055.md` (matches=14)
  Excerpt: terrain models (DTMs, the representative of data models in GIS), being represented as continuous field or discrete objects. They are derived by digital terrain analysis (a representative subdomain of spatial analysis) on the DTM recording elevation (or saying,...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-01-020.md` (matches=12)
  Excerpt: # AM-01-020 - Geospatial Analysis and Model Building Source: https://gistbok-ltb.ucgis.org/page/34/concept/10469 ## Introduction <p>Qiang, Y. (2021). Geospatial Analysis and Model Building.&nbsp;The Geographic Information Science &amp; Technology Body of Knowl...

### Learning Outcomes

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-01-028.md` (matches=9)
  Excerpt: h, a lesson&rsquo;s sequence may involve one or more strategies for ordering content. Sixth, a lesson&rsquo;s activity concerns what students do during a lesson and is often associated with different learning outcomes. These six variables help differentiate tr...
- `C:/Users/sounn/Git/gis/references/bok-mapping.md` (matches=3)
  Excerpt: *Body of Knowledge** (often referred to as **BoK** / **BoK2\*\*). It is intended as a *curriculum alignment backbone\*: - Make chapter scope explicit (what this chapter covers / does not cover). - Keep learning outcomes measurable and assessable. - Support covera...

### Key Terms

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/CV-04-033.md` (matches=2)
  Excerpt: ons of maps, narrative, and stories from cartography and data journalism to feminist mapping, Black geographies, and decolonial mapping to reveal the power of mapped stories. I begin by unpacking two key terms&mdash;story and narrative&mdash;and conclude by st...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-05-076.md` (matches=1)
  Excerpt: tions of Spatial Networks</li> <li>Other Algorithms</li> </ol> <h4>1. Definitions</h4> <p><span><span><span><span>To begin with the understanding of network analyses we need to get a hold of a few key terms that need to be defined early on:</span></span></span...

### The Analysis Workflow

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/PD-05-031.md` (matches=1)
  Excerpt: ublic GitHub repository</a>&nbsp;hosting aforementioned files and data sets. Interested readers can freely download this repository, build the conda environment the authors originally used, replicate the analysis workflow, and reproduce results of the paper. M...

### Buffering

- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-geospatial-analysis-i-vector-o.html` (matches=6)
  Excerpt: itable block" id="campbell_1.0-ch07_s01_p01">As the name suggests, single layer analyses are those that are undertaken on an individual feature dataset. <span class="margin_term"><a class="glossterm">Buffering</a><span class="glossdef">Placing a region of spec...
- `C:/Users/sounn/Git/gis/references/text_essentials-of-geographic-information-systems-master/s11-01-single-layer-analysis.html` (matches=5)
  Excerpt: itable block" id="campbell_1.0-ch07_s01_p01">As the name suggests, single layer analyses are those that are undertaken on an individual feature dataset. <span class="margin_term"><a class="glossterm">Buffering</a><span class="glossdef">Placing a region of spec...

### Interpolation

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-02-040.md` (matches=68)
  Excerpt: # AM-02-040 - Areal Interpolation Source: https://gistbok-ltb.ucgis.org/page/34/concept/10479 ## Introduction <p>Comber, A. and Zeng, W. (2022). Areal Interpolation. The Geographic Information Science &amp; Technology Body of Knowledge&nbsp;(2nd Quarter 2022 E...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-04-067.md` (matches=45)
  Excerpt: # AM-04-067 - Gridding, Interpolation, and Contouring Source: https://gistbok-ltb.ucgis.org/page/34/concept/10834 ## Introduction <p>Raposo, P. (2025). Gridding, Interpolation, and Contouring.&nbsp;&nbsp;The Geographic Information Science &amp; Technology Body...

### Theissen Polygons

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-05-043.md` (matches=1)
  Excerpt: etwork distance metric accordingly. Figures 2a and 2b show the service areas delineated for four supercenters using the Euclidean distance and network distance, respectively. &nbsp;</p> <p><img alt="Theissen polygons and service areas" src="https://bok-figures...

### Ian McHarg

- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/AM-03-012.md` (matches=1)
  Excerpt: d Rhind, 1991) to offer more powerful computational opportunities in environmental modeling and analysis (Nijhuis, 2016).</p> <p>One comprehensive explanation of cartographic modeling is provided by Ian McHarg&rsquo;s (1969) Design with Nature (although he did...
- `C:/Users/sounn/Git/gis/references/ucgis-bok/topics/DA-009.md` (matches=1)
  Excerpt: 2012).&nbsp; Though the term itself is relatively new, the intellectual concepts and techniques associated with geodesign are rooted in decades of research and practice beginning in the 1960s. &nbsp;Ian McHarg, at Penn, and Phil Lewis, at Wisconsin, were lands...

## Completed Adaptations (January 2026)

- [x] **Interactive module:** Added "Interactive: Suitability Studio" where students adjust weights for Nature, Road, and Slope to site an eco-lodge.
- [x] **Local-to-Global:** "The Woodlands: A McHargian Design" connecting George Mitchell's Texas community to McHarg's ecological planning.
- [x] **Important Persons:** Bio Box for Ian McHarg is present.
- [x] **Critical GIS:** Added "The Black Box of Weights" callout explaining how algorithms encode opinions (gentrification, etc.).
