/**
 * Lab Switcher JS
 * Handles toggling between ArcGIS Pro, QGIS, and Web GIS instructions.
 */

document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab-btn');
    const panes = document.querySelectorAll('.instruction-pane');

    // Function to switch platform
    const switchPlatform = (platform) => {
        // Update Tabs
        tabs.forEach(tab => {
            if (tab.dataset.platform === platform) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });

        // Update Panes
        panes.forEach(pane => {
            if (pane.dataset.platform === platform) {
                pane.classList.add('active');
            } else {
                pane.classList.remove('active');
            }
        });

        // Store preference
        localStorage.setItem('preferred-gis-platform', platform);
    };

    // Add click listeners
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            switchPlatform(tab.dataset.platform);
        });
    });

    // Load preferred platform
    const savedPlatform = localStorage.getItem('preferred-gis-platform') || 'arcgis';
    switchPlatform(savedPlatform);
});
