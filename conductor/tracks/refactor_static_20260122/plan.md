# Implementation Plan: Refactor Codebase for Static Deployment

## Phase 1: Structure & Cleanup
- [x] Task: Remove LMS Manifests <!-- 462ecd7 -->
    - [x] Identify and delete `imsmanifest.xml`.
- [x] Task: Standardize Asset Directories <!-- 3c33403 -->
    - [x] Ensure `assets/img/` contains all textbook images.
    - [x] Move any remaining media from `references/uf_canvas_extract/` to `assets/`.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Structure & Cleanup' (Protocol in workflow.md)

## Phase 2: Relative Pathing & Linking
- [ ] Task: Update CSS References
    - [ ] Audit `css/style.css` for absolute or broken URLs.
    - [ ] Update to relative paths.
- [ ] Task: Update HTML Internal Links
    - [ ] Audit `index.html` and `chapters/*.html`.
    - [ ] Replace `$IMS-CC-FILEBASE$` and similar placeholders with relative paths to `assets/`.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Relative Pathing & Linking' (Protocol in workflow.md)

## Phase 3: Final Integration
- [ ] Task: Verify Navigation
    - [ ] Ensure `index.html` links correctly to all 17 planned modules.
- [ ] Task: Cross-browser Smoke Test
    - [ ] Open site in Chrome and Firefox to verify static rendering.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Integration' (Protocol in workflow.md)