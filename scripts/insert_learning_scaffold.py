import re
from pathlib import Path
from typing import Optional, Dict, Any


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"


def scaffold_html(cfg: Dict[str, Any]) -> str:
    def li(items):
        return "\n".join([f"                        <li>{x}</li>" for x in items])

    def qa(items):
        out = []
        for q in items:
            out.append(
                """
                        <li>
                            <details>
                                <summary>{question}</summary>
                                <div>
                                    <p><strong>Answer:</strong> {answer}</p>
                                    <p><strong>Why:</strong> {why}</p>
                                    <p><strong>Common misconception:</strong> {misconception}</p>
                                </div>
                            </details>
                        </li>""".format(
                    **q
                ).strip("\n")
            )
        return "\n".join(out)

    return (
        """
        <section class="card learning-scaffold" aria-label="Learning scaffold">
            <div class="scaffold-head">
                <h2>At a Glance</h2>
                <div class="scaffold-meta" aria-label="Prerequisites and time estimate">
                    <span class="scaffold-chip"><strong>Prereqs:</strong> {prereqs}</span>
                    <span class="scaffold-chip"><strong>Time:</strong> {time}</span>
                    <span class="scaffold-chip"><strong>Deliverable:</strong> {deliverable}</span>
                </div>
            </div>

            <div class="scaffold-grid">
                <div class="scaffold-card">
                    <h3>Learning outcomes</h3>
                    <ul>
{outcomes}
                    </ul>
                </div>

                <div class="scaffold-card">
                    <h3>Key terms</h3>
                    <p>{key_terms}</p>
                </div>
            </div>

            <div class="scaffold-grid">
                <div class="scaffold-card">
                    <h3>Stop &amp; check</h3>
                    <ol class="scaffold-qa">
{stop_check}
                    </ol>
                </div>

                <div class="scaffold-card">
                    <h3>Try it (5 minutes)</h3>
                    <ol>
{try_it}
                    </ol>
                </div>
            </div>

            <div class="scaffold-grid">
                <div class="scaffold-card">
                    <h3>Lab (Two Tracks)</h3>
                    <p>{lab_intro}</p>
                    <div class="scaffold-two-track">
                        <div class="scaffold-track">
                            <h4>Desktop GIS Track (ArcGIS Pro / QGIS)</h4>
                            <p>{lab_desktop}</p>
                        </div>
                        <div class="scaffold-track">
                            <h4>Remote Sensing Track (Google Earth Engine)</h4>
                            <p>{lab_gee}</p>
                        </div>
                    </div>
                </div>

                <div class="scaffold-card">
                    <h3>Common mistakes</h3>
                    <ul>
{common_mistakes}
                    </ul>
                    <p><strong>Further reading:</strong> {further_reading}</p>
                </div>
            </div>
        </section>
"""
        .format(
            prereqs=cfg["prereqs"],
            time=cfg["time"],
            deliverable=cfg["deliverable"],
            outcomes=li(cfg["outcomes"]),
            key_terms=cfg["key_terms"],
            stop_check=qa(cfg["stop_check"]),
            try_it=li(cfg["try_it"]),
            lab_intro=cfg["lab_intro"],
            lab_desktop=cfg["lab_desktop"],
            lab_gee=cfg["lab_gee"],
            common_mistakes=li(cfg["common_mistakes"]),
            further_reading=cfg["further_reading"],
        )
        .rstrip()
    )


CFG_BY_CHAPTER = {
    "01": {
        "prereqs": "Chapter 00",
        "time": "20 min read + 20 min practice",
        "deliverable": "Raster vs vector decision note",
        "outcomes": [
            "Explain the difference between vector and raster models.",
            "Describe how resolution affects what you can see and measure.",
            "Choose the right model for a real GIS question and justify your choice.",
        ],
        "key_terms": "vector, raster, pixel, resolution, extent, topology",
        "stop_check": [
            {
                "question": "Which data model is best for utility pipelines: raster or vector?",
                "answer": "Vector (lines).",
                "why": "Pipelines are discrete objects with connectivity and attributes.",
                "misconception": "Aerial imagery shows pipelines, but the network itself is modeled as vector geometry.",
            },
            {
                "question": "If you increase raster resolution, what happens to pixel size?",
                "answer": "Pixel size decreases.",
                "why": "Higher resolution means smaller ground area per pixel.",
                "misconception": "\"Higher\" resolution does not mean bigger pixels; it changes measurement detail.",
            },
        ],
        "try_it": [
            "Toggle between raster and vector layers and zoom until you see pixels.",
            "Write one sentence: what stays sharp at any scale, and why?",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a 6-8 sentence decision note about which model fits a chosen problem.",
        "lab_desktop": "Add imagery + a vector layer (roads/parcels). Compare what questions each layer supports and include one screenshot.",
        "lab_gee": "Load a public image (Sentinel-2 or Landsat) and a vector AOI. Describe what is pixel-based vs feature-based in your map.",
        "common_mistakes": [
            "Confusing map scale with raster resolution.",
            "Assuming all rasters are photographs (many rasters store elevation, temperature, indices).",
            "Forgetting CRS/units when measuring distances/areas.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "02": {
        "prereqs": "Chapter 01",
        "time": "25 min read + 25 min practice",
        "deliverable": "One-page map layout",
        "outcomes": [
            "Identify the essential elements of a clear map.",
            "Choose a color scheme that matches the data and audience.",
            "Critique a map for clarity, honesty, and accessibility.",
        ],
        "key_terms": "visual hierarchy, legend, symbology, classification, color ramp, accessibility",
        "stop_check": [
            {
                "question": "When is a sequential color ramp appropriate?",
                "answer": "For ordered numeric data (low to high).",
                "why": "Sequential ramps communicate magnitude in one direction.",
                "misconception": "Random colors can hide ordering and mislead interpretation.",
            },
            {
                "question": "Why should a map include a data source and date?",
                "answer": "To support credibility and correct interpretation.",
                "why": "Spatial results are time- and source-dependent.",
                "misconception": "A nice-looking map is not automatically trustworthy without provenance.",
            },
        ],
        "try_it": [
            "Find one ""bad map"" online and list 3 specific design problems.",
            "Rewrite its title and legend text so a non-expert can understand it.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a single map export (PDF/PNG) plus a 5-bullet design rationale.",
        "lab_desktop": "Make a layout for an index or classification map (NDVI or land cover). Export and include map elements + citations.",
        "lab_gee": "Create a map view (true/false color or NDVI), add a legend and caption text in your report, and export a figure.",
        "common_mistakes": [
            "Using color that implies meaning you do not intend (e.g., red/green without explanation).",
            "Missing legend/title/source or using vague titles.",
            "Relying on color alone (no labels, patterns, or value ranges).",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "03": {
        "prereqs": "Chapters 01-02",
        "time": "25 min read + 25 min practice",
        "deliverable": "Projection choice memo",
        "outcomes": [
            "Distinguish datum, projection, and CRS in practical terms.",
            "Predict and explain distortion patterns for common projections.",
            "Select a CRS for measurement and justify the choice.",
        ],
        "key_terms": "CRS, datum, projection, EPSG, Web Mercator, UTM, distortion",
        "stop_check": [
            {
                "question": "Why is Web Mercator a poor choice for area calculations?",
                "answer": "It distorts area (especially away from the equator).",
                "why": "It was designed for web mapping convenience, not measurement accuracy.",
                "misconception": "If it looks right on screen, it must measure right.",
            },
            {
                "question": "When is UTM a good default?",
                "answer": "For local/regional work within one UTM zone.",
                "why": "It preserves distance/area reasonably well locally in meters.",
                "misconception": "UTM is a single global CRS; it is a zone system.",
            },
        ],
        "try_it": [
            "Pick one city-sized AOI and write the unit you want for distance (meters or degrees).",
            "Explain in one sentence why your unit choice matters for buffers.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a short memo (8-10 sentences) recommending a CRS for a stated task.",
        "lab_desktop": "Reproject one layer and measure a distance/area. Compare results before/after and include one screenshot.",
        "lab_gee": "Load an AOI and compute a simple area/distance summary. Note the CRS/projection assumptions in your memo.",
        "common_mistakes": [
            "Measuring distance/area in geographic coordinates (degrees).",
            "Mixing layers with different CRS without noticing.",
            "Assuming EPSG codes imply the same units everywhere.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "04": {
        "prereqs": "Chapter 03",
        "time": "20 min read + 20 min practice",
        "deliverable": "Field collection plan",
        "outcomes": [
            "Explain how GNSS positioning works at a high level.",
            "Identify factors that reduce accuracy (multipath, poor geometry).",
            "Plan a basic field collection workflow for validation/GCPs.",
        ],
        "key_terms": "GNSS, trilateration, multipath, DOP, differential correction, datum",
        "stop_check": [
            {
                "question": "What usually causes multipath error?",
                "answer": "Signals reflecting off buildings/terrain before reaching the receiver.",
                "why": "Reflections increase path length and bias the range estimate.",
                "misconception": "More satellites always guarantees better accuracy; geometry and environment matter.",
            },
            {
                "question": "Why does CRS/datum matter for GNSS points?",
                "answer": "Because coordinates depend on the reference model used.",
                "why": "A mismatch can create consistent offsets between layers.",
                "misconception": "Latitude/longitude is ""universal"" and automatically matches every map.",
            },
        ],
        "try_it": [
            "List 3 places on campus/city where GNSS accuracy would likely be poor.",
            "For each, write one mitigation (move, wait, repeat, use correction).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a one-page plan describing how you would collect validation points for an imagery analysis.",
        "lab_desktop": "Design a point feature class or form schema (fields + domains). Define required metadata (time, accuracy, notes).",
        "lab_gee": "Define an AOI and draft a validation sampling plan (how many points per class and where you would collect them).",
        "common_mistakes": [
            "Collecting points with unknown CRS/datum or missing metadata.",
            "Taking one reading and assuming it is correct (no repeats).",
            "Collecting under tree canopy/near buildings without noting expected error.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
    "06": {
        "prereqs": "Chapters 01, 05",
        "time": "25 min read + 30 min practice",
        "deliverable": "Digitized training polygons",
        "outcomes": [
            "Digitize clean vector features with appropriate vertex density.",
            "Apply basic QA checks (snapping, no gaps/overlaps).",
            "Explain how digitizing choices affect analysis and classification.",
        ],
        "key_terms": "digitizing, snapping, topology, vertex, attribute table, training data",
        "stop_check": [
            {
                "question": "Why is snapping important when digitizing adjacent polygons?",
                "answer": "It prevents gaps and overlaps.",
                "why": "Topological errors propagate into area totals and overlays.",
                "misconception": "Tiny errors do not matter; they can create thousands of slivers in analysis.",
            },
            {
                "question": "Why do digitized training labels affect classification results?",
                "answer": "The model learns whatever you label as truth.",
                "why": "Label bias and mixed pixels reduce separability and accuracy.",
                "misconception": "More labels always helps; better labels and balance matters more.",
            },
        ],
        "try_it": [
            "Digitize one simple polygon and zoom in to inspect edges.",
            "List one place where you should avoid digitizing (ambiguous boundary).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a small set of labeled polygons (3-5 classes) plus a short QA note.",
        "lab_desktop": "Digitize training polygons on imagery, add class attribute, and run a topology/geometry check. Export GeoPackage/GeoJSON.",
        "lab_gee": "Create a FeatureCollection of training polygons (drawing tools) and export it. Write a QA note about class balance.",
        "common_mistakes": [
            "Over-digitizing: too many vertices without adding accuracy.",
            "Labeling mixed pixels (boundaries) as pure classes.",
            "Forgetting to record class definitions (what counts as ""forest"" vs ""shrub""?).",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "07": {
        "prereqs": "Chapter 06",
        "time": "25 min read + 30 min practice",
        "deliverable": "Joined table + short interpretation",
        "outcomes": [
            "Explain keys and relationships (one-to-many) in GIS tables.",
            "Perform a join and verify the result.",
            "Write one interpretation based on a query or summary.",
        ],
        "key_terms": "primary key, foreign key, join, query, null, domain",
        "stop_check": [
            {
                "question": "What is the most common reason a join produces many nulls?",
                "answer": "The key fields do not match (type/format/values).",
                "why": "Joins require exact matches; '001' is not the same as '1'.",
                "misconception": "The software is broken; usually the identifiers are inconsistent.",
            },
            {
                "question": "Why store acquisition date and cloud percent for imagery scenes?",
                "answer": "To filter and reproduce your analysis.",
                "why": "Time and quality strongly affect RS results.",
                "misconception": "A composite is ""one image""; it is a documented set of choices.",
            },
        ],
        "try_it": [
            "Write one query you would use to filter out low-quality data.",
            "Explain what ""null"" means in one sentence.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a small table summary (counts/means) plus a 6-sentence interpretation.",
        "lab_desktop": "Create a table, join it to a layer, and compute one summary (count/mean) by category.",
        "lab_gee": "Attach metadata properties to features (date/class) and compute a grouped summary using reducers. Explain the result.",
        "common_mistakes": [
            "Joining on non-unique fields.",
            "Mixing numeric and text IDs.",
            "Not checking row counts before/after joins.",
        ],
        "further_reading": "https://gistbok-topics.ucgis.org/UCGIS",
    },
    "07b": {
        "prereqs": "Chapters 09-10",
        "time": "15 min explore + 15 min write",
        "deliverable": "Band composite choice",
        "outcomes": [
            "Explain why different band combinations reveal different features.",
            "Select a band composite for a stated monitoring goal.",
            "Describe what you expect to see before you view it.",
        ],
        "key_terms": "spectral band, composite, false color, NIR, SWIR",
        "stop_check": [
            {
                "question": "Why can false color help you find vegetation stress?",
                "answer": "Because NIR/SWIR responses change before visible color changes.",
                "why": "Vegetation reflectance shifts across bands based on water content and structure.",
                "misconception": "False color is only for aesthetics; it is an analysis tool.",
            },
            {
                "question": "What should you do before trusting a composite interpretation?",
                "answer": "Know which bands are mapped to RGB and what they represent.",
                "why": "A color in the image is a mapping choice, not a literal surface color.",
                "misconception": "Red always means hot or danger; in RS it may mean vegetation (NIR mapped to red).",
            },
        ],
        "try_it": [
            "Pick a goal (water, burn scar, vegetation). Predict which composite will work best.",
            "Use the simulator and write 2 observations about what changed.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a 1-paragraph explanation of a chosen composite plus one annotated screenshot.",
        "lab_desktop": "Load a multispectral raster and create two RGB composites. Export one figure and annotate 3 features.",
        "lab_gee": "Load Sentinel-2 and visualize two composites (true color + false color). Export a figure and annotate 3 features.",
        "common_mistakes": [
            "Confusing display stretch with real reflectance.",
            "Comparing composites without matching date/season.",
            "Ignoring clouds and haze.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
    "08": {
        "prereqs": "Chapters 01, 06",
        "time": "20 min read + 25 min practice",
        "deliverable": "VGI quality critique",
        "outcomes": [
            "Explain what VGI is and why it can be powerful and risky.",
            "Identify at least three VGI quality dimensions.",
            "Design a simple QA plan using imagery or authoritative data as reference.",
        ],
        "key_terms": "VGI, completeness, positional accuracy, bias, conflation, metadata",
        "stop_check": [
            {
                "question": "What is one reason VGI can be biased?",
                "answer": "Contributions are uneven across places and communities.",
                "why": "Participation varies by access, interest, and events.",
                "misconception": "Crowdsourced means objective; it can reflect systematic gaps.",
            },
            {
                "question": "How can satellite imagery support VGI QA?",
                "answer": "By providing a consistent visual reference for feature presence/location.",
                "why": "Imagery can help validate geometry and completeness.",
                "misconception": "Imagery is always truth; it also has date, resolution, and interpretation limits.",
            },
        ],
        "try_it": [
            "Find one missing feature in a map you use (path/building/landmark) and describe how you would verify it.",
            "Write one sentence: what evidence would you cite?",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a 1-page QA note evaluating a small VGI area (completeness, accuracy, and bias).",
        "lab_desktop": "Compare a VGI layer to imagery for a small AOI. Mark 3 discrepancies and propose fixes.",
        "lab_gee": "Load imagery for an AOI and overlay a vector layer. Document 3 features that agree/disagree and explain why.",
        "common_mistakes": [
            "Treating VGI as authoritative without checking.",
            "Ignoring date mismatches between imagery and edits.",
            "Conflating ""no data"" with ""no feature"".",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "09": {
        "prereqs": "Chapters 01, 07",
        "time": "25 min read + 25 min practice",
        "deliverable": "Index interpretation note",
        "outcomes": [
            "Explain what a spectral signature represents.",
            "Predict how vegetation, soil, and water differ across bands.",
            "Compute and interpret one simple spectral index conceptually (e.g., NDVI).",
        ],
        "key_terms": "reflectance, spectral signature, band, NIR, SWIR, index",
        "stop_check": [
            {
                "question": "Why does healthy vegetation look bright in NIR?",
                "answer": "Leaf structure strongly reflects NIR.",
                "why": "Cell structure causes high NIR reflectance while chlorophyll absorbs red.",
                "misconception": "NIR means heat; thermal infrared is the ""heat"" region.",
            },
            {
                "question": "Why is water often dark in NIR?",
                "answer": "Water absorbs NIR strongly.",
                "why": "Absorption reduces reflected energy back to the sensor.",
                "misconception": "Dark pixels always mean shadow; it can be material absorption.",
            },
        ],
        "try_it": [
            "Pick one surface (water/vegetation/soil) and predict which band will separate it best.",
            "Check the simulator and write one corrected prediction.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a short write-up explaining one index and what it measures.",
        "lab_desktop": "Compute or visualize NDVI from a multispectral image and interpret high/low values in your AOI.",
        "lab_gee": "Load Sentinel-2/Landsat, compute NDVI, and export a figure. Describe what the index highlights and what it confuses.",
        "common_mistakes": [
            "Interpreting an index without checking season/date.",
            "Comparing scenes with different atmospheric conditions without correction.",
            "Assuming a single index answers every question.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
    "11": {
        "prereqs": "Chapters 09-10",
        "time": "30 min read + 35 min practice",
        "deliverable": "Confusion matrix + short interpretation",
        "outcomes": [
            "Explain the difference between training and validation data.",
            "Describe what a confusion matrix measures and how to read it.",
            "Identify one likely source of classification error and propose a fix.",
        ],
        "key_terms": "training data, validation, classifier, features, confusion matrix, overfitting",
        "stop_check": [
            {
                "question": "Why should training and validation samples be separate?",
                "answer": "To test generalization honestly.",
                "why": "Re-using training data inflates accuracy and hides overfitting.",
                "misconception": "More accuracy numbers means better; quality of evaluation matters.",
            },
            {
                "question": "What does high confusion between two classes usually mean?",
                "answer": "Their spectral/feature signatures overlap in your data.",
                "why": "The model cannot separate them with the current features/training.",
                "misconception": "The algorithm is bad; often the labels/features need improvement.",
            },
        ],
        "try_it": [
            "Name two classes that might be confused in your region (e.g., bare soil vs urban).",
            "List one extra feature you would add (SWIR, NDVI, texture, elevation).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a classified map plus a brief accuracy assessment statement.",
        "lab_desktop": "Create training polygons, run a supervised classification, and evaluate accuracy with a validation sample.",
        "lab_gee": "Train a classifier (e.g., RF), classify an image, and compute an error matrix. Interpret 2 key errors.",
        "common_mistakes": [
            "Train/validation leakage (same polygons used for both).",
            "Class imbalance (too few samples for minority classes).",
            "Mixing seasons/dates so the same class looks different.",
        ],
        "further_reading": "https://gistbok-topics.ucgis.org/UCGIS",
    },
    "12": {
        "prereqs": "Chapters 10-11",
        "time": "25 min read + 30 min practice",
        "deliverable": "DEM/DSM interpretation figure",
        "outcomes": [
            "Explain what LiDAR measures and what a point cloud represents.",
            "Distinguish DEM, DSM, and derived height models.",
            "Interpret a 3D product for a practical question (buildings/vegetation/terrain).",
        ],
        "key_terms": "LiDAR, point cloud, return, intensity, DEM, DSM, nDSM/CHM",
        "stop_check": [
            {
                "question": "Why can LiDAR measure ground under trees better than optical imagery?",
                "answer": "Some pulses penetrate canopy gaps and return from the ground.",
                "why": "Multiple returns capture vertical structure.",
                "misconception": "LiDAR is a photo; it is active ranging.",
            },
            {
                "question": "What does DSM minus DEM represent?",
                "answer": "Height above ground (a normalized surface).",
                "why": "Subtracting terrain removes elevation baseline.",
                "misconception": "DEM and DSM are interchangeable; they measure different surfaces.",
            },
        ],
        "try_it": [
            "Look at one hill and one building in the examples. Predict which surface (DEM/DSM) will show each.",
            "Write one sentence describing why.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a figure comparing DEM vs DSM plus a short interpretation paragraph.",
        "lab_desktop": "Load a LiDAR-derived DEM and DSM, compute a normalized height surface, and annotate one feature.",
        "lab_gee": "Load an elevation/DSM-like product (or provided sample) and compute a simple difference surface; interpret.",
        "common_mistakes": [
            "Using the wrong surface for a question (terrain vs objects).",
            "Forgetting units/resolution and over-interpreting noise.",
            "Confusing canopy height (CHM) with building height unless explicitly derived.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "13": {
        "prereqs": "Chapters 01, 10",
        "time": "30 min read + 35 min practice",
        "deliverable": "Raster workflow result map",
        "outcomes": [
            "Apply basic map algebra operations to rasters.",
            "Explain how NoData and alignment affect results.",
            "Build a small raster workflow tied to an RS product (index, DEM).",
        ],
        "key_terms": "map algebra, NoData, resampling, alignment, focal/zonal operations",
        "stop_check": [
            {
                "question": "Why do two rasters need matching alignment and cell size for map algebra?",
                "answer": "So each cell-to-cell operation compares the correct locations.",
                "why": "Misalignment mixes different ground locations and creates artifacts.",
                "misconception": "Reprojection alone guarantees alignment; you often need a snap raster.",
            },
            {
                "question": "What does NoData usually do in calculations?",
                "answer": "It propagates (many operations output NoData).",
                "why": "Undefined inputs lead to undefined results unless handled explicitly.",
                "misconception": "NoData equals zero; it means missing/invalid.",
            },
        ],
        "try_it": [
            "Predict what happens if you add two rasters with different resolutions.",
            "Write one sentence: what choice does the software have to make?",
        ],
        "lab_intro": "Both tracks produce the same deliverable: one raster analysis output plus a 6-sentence methods note.",
        "lab_desktop": "Run a reclass or focal statistic on an index/DEM and produce a map with a legend.",
        "lab_gee": "Compute an index (e.g., NDVI) and apply a threshold or neighborhood operation. Export a figure.",
        "common_mistakes": [
            "Mixing meters and degrees in distance-based rasters.",
            "Ignoring NoData masks and interpreting gaps as low values.",
            "Comparing rasters from different dates without stating it.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
    "14": {
        "prereqs": "Chapters 06, 13",
        "time": "30 min read + 30 min practice",
        "deliverable": "Vector analysis result layer",
        "outcomes": [
            "Choose the correct vector operation for a question (buffer, overlay, join).",
            "Explain how projection/units affect vector measurements.",
            "Validate results by checking counts, areas, and obvious edge cases.",
        ],
        "key_terms": "buffer, dissolve, intersect, union, spatial join, slivers",
        "stop_check": [
            {
                "question": "Why can buffering in degrees produce nonsense results?",
                "answer": "Degrees are angular units and vary in ground distance by latitude.",
                "why": "Buffer distance needs linear units like meters.",
                "misconception": "A buffer of 0.01 degrees is ""about"" the same everywhere.",
            },
            {
                "question": "What are slivers after overlay and why do they matter?",
                "answer": "Tiny polygons created by boundary mismatch.",
                "why": "They inflate feature counts and can bias area summaries.",
                "misconception": "They are harmless; they can dominate statistics when many exist.",
            },
        ],
        "try_it": [
            "Pick one question and name the operation: ""within 500m"", ""overlaps"", or ""closest"".",
            "Write one sentence explaining your tool choice.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: one derived vector layer plus a short QA checklist.",
        "lab_desktop": "Run one buffer + one overlay (intersect) and report feature counts before/after.",
        "lab_gee": "Create buffers around points/lines (where applicable) and summarize an image statistic inside the buffer. Report results.",
        "common_mistakes": [
            "Forgetting to dissolve buffers when you need a single influence zone.",
            "Interpreting overlay without checking attributes and geometry validity.",
            "Assuming spatial joins are reversible; direction matters.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "15": {
        "prereqs": "Chapters 13-14",
        "time": "30 min read + 40 min build",
        "deliverable": "Model workflow diagram",
        "outcomes": [
            "Explain what a spatial model is (workflow + assumptions).",
            "Identify inputs, parameters, and outputs for a modeling task.",
            "Document a model so someone else can reproduce it.",
        ],
        "key_terms": "workflow, parameters, reproducibility, suitability model, validation",
        "stop_check": [
            {
                "question": "Why should model parameters be documented?",
                "answer": "Because they control outputs and enable reproducibility.",
                "why": "A model without parameters is not interpretable or repeatable.",
                "misconception": "The software remembers; your reader or future self does not.",
            },
            {
                "question": "What is one way to validate a model output?",
                "answer": "Compare to independent data or holdout samples.",
                "why": "Validation checks whether the model predicts known conditions.",
                "misconception": "A nice-looking map implies correctness.",
            },
        ],
        "try_it": [
            "Write the 3 inputs you would use for a suitability model (any topic).",
            "Write one parameter choice you must justify (threshold, weights, distance).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a workflow diagram plus a 1-page methods explanation.",
        "lab_desktop": "Build a simple ModelBuilder/processing model and export the diagram. Include parameter values.",
        "lab_gee": "Write a small scripted workflow (filter, composite, index, threshold). Document parameters and export a figure.",
        "common_mistakes": [
            "Hardcoding paths/dates so the model cannot be reused.",
            "Using weights without justification or sensitivity checks.",
            "Skipping validation entirely.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
    "16": {
        "prereqs": "Chapters 04, 06",
        "time": "25 min read + 30 min practice",
        "deliverable": "Field form + QA checklist",
        "outcomes": [
            "Design a mobile data collection form that reduces errors.",
            "Explain how location accuracy and metadata affect analysis.",
            "Connect field data to remote sensing validation workflows.",
        ],
        "key_terms": "offline, domains, validation rules, positional accuracy, privacy, metadata",
        "stop_check": [
            {
                "question": "Why use domains (restricted value lists) in a field form?",
                "answer": "To prevent typos and enforce consistency.",
                "why": "Consistent categories enable reliable summaries and training labels.",
                "misconception": "Free text is more flexible; it often breaks analysis later.",
            },
            {
                "question": "What metadata is critical for a field photo point?",
                "answer": "Date/time, accuracy estimate, and a clear class/label.",
                "why": "Validation requires knowing when/where and what the observation represents.",
                "misconception": "A photo alone is enough; without metadata it is hard to trust and reuse.",
            },
        ],
        "try_it": [
            "Write 5 fields you would collect for a land cover validation point.",
            "Mark which fields should be required.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a form schema and a one-page QA plan for field collection.",
        "lab_desktop": "Create a feature layer schema (fields + domains) and draft collection instructions for a team.",
        "lab_gee": "Design a validation sampling plan (how many points, where, what classes) that your field form would support.",
        "common_mistakes": [
            "Not recording accuracy or confidence in the observation.",
            "Collecting points without privacy/safety considerations.",
            "Inconsistent class definitions across collectors.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "17": {
        "prereqs": "Chapters 02, 10",
        "time": "25 min read + 35 min build",
        "deliverable": "Story map outline",
        "outcomes": [
            "Plan a geospatial narrative with a clear question and evidence.",
            "Choose visuals that match the message and uncertainty.",
            "Write a short methods-and-limits statement for credibility.",
        ],
        "key_terms": "narrative, audience, evidence, annotation, uncertainty, citation",
        "stop_check": [
            {
                "question": "What is the difference between storytelling and decoration?",
                "answer": "Storytelling ties visuals to a claim supported by data and methods.",
                "why": "A map should answer a question, not only look good.",
                "misconception": "More layers equals more insight; clarity and relevance matter.",
            },
            {
                "question": "Why include limitations in a story map?",
                "answer": "To prevent over-interpretation and build trust.",
                "why": "Spatial data has uncertainty, dates, and classification errors.",
                "misconception": "Limitations weaken the story; they strengthen credibility.",
            },
        ],
        "try_it": [
            "Write a one-sentence story question (e.g., ""Where did flooding expand?"").",
            "List 2 datasets that could serve as evidence (one should be imagery-derived).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a storyboard (6 panels) with titles, captions, and a cited figure list.",
        "lab_desktop": "Create two maps (context + result) and draft the narrative captions and sources.",
        "lab_gee": "Export one imagery-derived figure (index/classification) and write captions that interpret it responsibly.",
        "common_mistakes": [
            "Writing conclusions not supported by the map/analysis.",
            "Omitting dates and sources.",
            "Using misleading symbology or color ramps without explanation.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "18": {
        "prereqs": "None",
        "time": "25 min read + 20 min scenarios",
        "deliverable": "Ethics checklist",
        "outcomes": [
            "Identify ethical risks in common GIS/RS workflows.",
            "Explain how bias and uncertainty can harm decisions.",
            "Apply a simple checklist before sharing spatial outputs.",
        ],
        "key_terms": "privacy, bias, uncertainty, consent, provenance, model card",
        "stop_check": [
            {
                "question": "Why can point maps reveal sensitive information even without names?",
                "answer": "Locations can re-identify people or sensitive sites.",
                "why": "Spatial data can be inherently identifying.",
                "misconception": "Removing names is enough; geometry can still expose.",
            },
            {
                "question": "What is one ethical risk of using AI classification outputs?",
                "answer": "Over-trusting outputs without validation and bias checks.",
                "why": "Models encode training data biases and can fail in new contexts.",
                "misconception": "AI is objective; it is data- and assumption-dependent.",
            },
        ],
        "try_it": [
            "Take one map you made previously and list 2 ways it could mislead.",
            "Write one fix (aggregation, caveat, validation, better legend).",
        ],
        "lab_intro": "Both tracks produce the same deliverable: an ethics review checklist completed for a chosen mapping scenario.",
        "lab_desktop": "Pick a dataset and write a short ""share/not share"" decision with mitigation steps.",
        "lab_gee": "Pick an imagery workflow and write how you will document uncertainty (clouds, classification errors, dates).",
        "common_mistakes": [
            "Publishing precise points for sensitive phenomena.",
            "Not documenting uncertainty or validation.",
            "Equating model output with ground truth.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "19": {
        "prereqs": "Chapters 15-18",
        "time": "25 min read + 35 min cleanup",
        "deliverable": "Project README + metadata",
        "outcomes": [
            "Organize a GIS/RS project for reproducibility.",
            "Write a minimal README and metadata record.",
            "Choose an appropriate license and citation format.",
        ],
        "key_terms": "metadata, provenance, DOI, licensing, reproducibility, versioning",
        "stop_check": [
            {
                "question": "Why is CRS information part of metadata?",
                "answer": "Because coordinates and measurements depend on CRS.",
                "why": "Without CRS, data can be misaligned or mis-measured.",
                "misconception": "A shapefile ""knows"" its CRS; it often does not travel reliably without metadata.",
            },
            {
                "question": "What is a good alternative to 'final_v7_reallyfinal'?",
                "answer": "Semantic versioning and a changelog (or dated releases).",
                "why": "Clear versioning supports replication and comparison.",
                "misconception": "You will remember later; project history becomes unreadable fast.",
            },
        ],
        "try_it": [
            "Create a folder structure: data/raw, data/processed, outputs, scripts, docs.",
            "Write 5 README bullets describing data sources and processing steps.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a clean project structure plus a README that another student can run.",
        "lab_desktop": "Package a small project with inputs, outputs, and a methods log. Export one final figure.",
        "lab_gee": "Document your script inputs (AOI, dates, bands), export outputs, and write a methods + provenance note.",
        "common_mistakes": [
            "Editing raw data instead of writing processed outputs.",
            "Not recording acquisition dates or processing level.",
            "Sharing outputs without listing parameters and versions.",
        ],
        "further_reading": "https://www.ucgis.org/site/gis-t-body-of-knowledge",
    },
    "20": {
        "prereqs": "Chapter 19",
        "time": "30 min read + 45 min draft",
        "deliverable": "Mini research proposal",
        "outcomes": [
            "Formulate a research question suitable for GIS/remote sensing.",
            "Choose data and methods that answer the question.",
            "Describe how you will validate results and report limitations.",
        ],
        "key_terms": "research question, hypothesis, operationalization, validation, uncertainty, ethics",
        "stop_check": [
            {
                "question": "What makes a GIS question ""researchable"" (not just a map request)?",
                "answer": "It requires a method, evidence, and evaluation of uncertainty.",
                "why": "Research creates new knowledge or tests a claim.",
                "misconception": "Any map equals research; research must be defendable and reproducible.",
            },
            {
                "question": "Why must methods include validation?",
                "answer": "To quantify error and prevent over-claiming.",
                "why": "Spatial results can be wrong for systematic reasons.",
                "misconception": "A model output is correct if it runs without errors.",
            },
        ],
        "try_it": [
            "Write one research question and one measurable outcome variable.",
            "List 2 datasets and one validation source.",
        ],
        "lab_intro": "Both tracks produce the same deliverable: a 1-2 page proposal (question, data, method, validation, ethics, timeline).",
        "lab_desktop": "Draft your proposal and include one figure showing your AOI and planned layers.",
        "lab_gee": "Draft your proposal and include one figure from a quick exploratory script (composite/index).",
        "common_mistakes": [
            "Questions that are too broad to answer with available data.",
            "Methods that do not match the question.",
            "No validation plan.",
        ],
        "further_reading": "https://gistbok-ltb.ucgis.org/",
    },
}


def select_cfg(path: Path) -> Optional[Dict[str, Any]]:
    name = path.name

    m = re.match(r"chapter-(\d\d)-", name)
    if not m:
        return None
    ch = m.group(1)

    # Special case: band combiner is named as chapter-07-band-combiner.html
    if ch == "07" and "band-combiner" in name:
        return CFG_BY_CHAPTER["07b"]
    return CFG_BY_CHAPTER.get(ch)


def insert_after_nav(html: str, insert: str) -> Optional[str]:
    # Insert after the first </nav> inside main container.
    idx_main = html.find("<main")
    if idx_main == -1:
        return None

    idx_nav_end = html.find("</nav>", idx_main)
    if idx_nav_end == -1:
        return None
    idx_nav_end += len("</nav>")
    return html[:idx_nav_end] + "\n\n" + insert + "\n" + html[idx_nav_end:]


def main() -> int:
    paths = sorted(CHAPTERS_DIR.glob("chapter-*.html"))
    updated = 0
    skipped = 0

    for p in paths:
        text = p.read_text(encoding="utf-8", errors="ignore")
        if "learning-scaffold" in text:
            skipped += 1
            continue

        cfg = select_cfg(p)
        if not cfg:
            # If we cannot identify config, skip rather than insert placeholders.
            skipped += 1
            continue

        block = scaffold_html(cfg)
        out = insert_after_nav(text, block)
        if not out:
            skipped += 1
            continue

        p.write_text(out, encoding="utf-8", newline="\n")
        updated += 1

    print(f"Updated: {updated}; Skipped: {skipped}; Total: {len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
