# Implementation Plan: Refactor Codebase for Static Deployment

## Phase 1: Structure & Cleanup [checkpoint: 326442a]
- [x] Task: Remove LMS Manifests <!-- 462ecd7 -->
    - [x] Identify and delete `imsmanifest.xml`.
- [x] Task: Standardize Asset Directories <!-- 3c33403 -->
    - [x] Ensure `assets/img/` contains all textbook images.
    - [x] Move any remaining media from `references/uf_canvas_extract/` to `assets/`.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Structure & Cleanup' (Protocol in workflow.md)

## Phase 2: Relative Pathing & Linking [checkpoint: 6a8ac8e]

- [x] Task: Update CSS References <!-- 5f35c33 -->

    - [x] Audit `css/style.css` for absolute or broken URLs.

    - [x] Update to relative paths.

- [x] Task: Update HTML Internal Links <!-- cab1961 -->

    - [x] Audit `index.html` and `chapters/*.html`.

    - [x] Replace `$IMS-CC-FILEBASE# Implementation Plan: Refactor Codebase for Static Deployment

## Phase 1: Structure & Cleanup [checkpoint: 326442a]
- [x] Task: Remove LMS Manifests <!-- 462ecd7 -->
    - [x] Identify and delete `imsmanifest.xml`.
- [x] Task: Standardize Asset Directories <!-- 3c33403 -->
    - [x] Ensure `assets/img/` contains all textbook images.
    - [x] Move any remaining media from `references/uf_canvas_extract/` to `assets/`.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Structure & Cleanup' (Protocol in workflow.md)
 and similar placeholders with relative paths to `assets/`.

- [x] Task: Conductor - User Manual Verification 'Phase 2: Relative Pathing & Linking' (Protocol in workflow.md)



## Phase 3: Final Integration



- [x] Task: Verify Navigation <!-- d362264 -->



    - [x] Ensure `index.html` links correctly to all 17 planned modules.









- [ ] Task: Cross-browser Smoke Test

    - [ ] Open site in Chrome and Firefox to verify static rendering.

- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Integration' (Protocol in workflow.md)
