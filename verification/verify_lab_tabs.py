import os
import http.server
import socketserver
import threading
import re
import random
from playwright.sync_api import sync_playwright, expect

# Global flag to stop the server
stop_server = False

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run_server(port):
    try:
        with socketserver.TCPServer(("", port), QuietHandler) as httpd:
            while not stop_server:
                httpd.handle_request()
    except Exception as e:
        print(f"Server error: {e}")

def verify_tabs():
    global stop_server

    port = random.randint(8001, 8999)

    # Start server in a background thread
    server_thread = threading.Thread(target=run_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Use localhost to avoid file path issues
            url = f"http://localhost:{port}/labs/lab-07-remote-sensing.html"

            # Intercept and block external assets
            page.route("**/*", lambda route: route.abort() if any(domain in route.request.url for domain in ["youtube.com", "google.com", "googleapis.com", "gstatic.com"]) else route.continue_())

            page.goto(url, wait_until="domcontentloaded")

            # Initial state: ArcGIS Pro should be active
            arcgis_btn = page.get_by_role("button", name="ArcGIS Pro")
            expect(arcgis_btn).to_have_class(re.compile(r"active"))
            expect(page.locator("#arcgis")).to_be_visible()

            # Click QGIS tab
            qgis_btn = page.get_by_role("button", name="QGIS")
            qgis_btn.click()

            # Verify QGIS is active
            expect(qgis_btn).to_have_class(re.compile(r"active"))
            expect(arcgis_btn).not_to_have_class(re.compile(r"active"))
            expect(page.locator("#qgis")).to_be_visible()
            expect(page.locator("#arcgis")).not_to_be_visible()

            # Take screenshot of active QGIS tab
            page.screenshot(path="verification/qgis_tab_active.png", animations="disabled")

            # Click GEE tab
            gee_btn = page.get_by_role("button", name="Google Earth Engine")
            gee_btn.click()

            # Verify GEE is active
            expect(gee_btn).to_have_class(re.compile(r"active"))
            expect(page.locator("#gee")).to_be_visible()

            # Take screenshot of active GEE tab
            page.screenshot(path="verification/gee_tab_active.png", animations="disabled")

            browser.close()
    finally:
        stop_server = True
        # One last dummy request to unblock the server thread's handle_request()
        import urllib.request
        try:
            urllib.request.urlopen(f"http://localhost:{port}")
        except:
            pass

if __name__ == "__main__":
    verify_tabs()
