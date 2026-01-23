# Specification: Refactor Codebase for Static Deployment

## Goal
Convert the existing IMS Common Cartridge based GIS textbook structure into a standard, browser-native static web directory structure suitable for hosting on GitHub Pages.

## Scope
- Remove LMS-specific manifest files (`imsmanifest.xml`).
- Standardize folder structure (`chapters/`, `assets/`, `css/`, `js/`).
- Update all internal links (images, styles, scripts) to use relative paths.
- Ensure the `index.html` serves as the primary entry point for the textbook.

## Technical Requirements
- Pure HTML5/CSS3/Vanilla JS.
- No build process or frameworks.
- Relative URL pathing for portability.

## Acceptance Criteria
- Website loads correctly in a browser without an LMS environment.
- All images and CSS styles render without console errors.
- Navigation between chapters works via relative links.
- Codebase is free of IMS/XML metadata files.