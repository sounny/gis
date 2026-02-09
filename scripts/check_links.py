import os
import re
from pathlib import Path
from urllib.parse import unquote

def check_chapters(chapters_dir):
    chapters_path = Path(chapters_dir)
    html_files = sorted(list(chapters_path.glob("*.html")))
    
    report = []
    
    print(f"Checking {len(html_files)} chapters in {chapters_path}...")

    total_errors = 0

    for file_path in html_files:
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            report.append(f"ERROR: Could not read {file_path.name}: {e}")
            continue

        # Simple regex to find links and images
        # This is not perfect HTML parsing but good enough for checking validity in well-formed files
        # Matches href="..." or src="..."
        links = re.findall(r'href=["\'](.*?)["\']', content)
        images = re.findall(r'src=["\'](.*?)["\']', content)
        
        file_errors = []

        # Check links
        for link in links:
            if link.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                continue # Skip external links
            if link.startswith('#'):
                continue # Skip internal anchors for now
            if link.startswith('javascript:'):
                continue
                
            # Handle anchors in file paths (e.g. page.html#section)
            link_clean = link.split('#')[0]
            if not link_clean:
                continue
                
            # Check existence
            target_path = (file_path.parent / link_clean).resolve()
            
            # Handle potential query params ?v=...
            target_path_str = str(target_path).split('?')[0]
            target_path = Path(target_path_str)

            if not target_path.exists():
                # Try unquoting
                decoded_link = unquote(link_clean)
                target_path_decoded = (file_path.parent / decoded_link).resolve()
                target_path_decoded_str = str(target_path_decoded).split('?')[0]
                target_path_decoded = Path(target_path_decoded_str)
                
                if not target_path_decoded.exists():
                     file_errors.append(f"Broken Link: {link} (resolved: {target_path_str})")

        # Check images
        for img in images:
            if img.startswith(('http://', 'https://', 'data:')):
                continue
                
            target_path = (file_path.parent / img).resolve()
            target_path_str = str(target_path).split('?')[0]
            target_path = Path(target_path_str)
            
            if not target_path.exists():
                 # Try unquoting
                decoded_img = unquote(img)
                target_path_decoded = (file_path.parent / decoded_img).resolve()
                target_path_decoded_str = str(target_path_decoded).split('?')[0]
                target_path_decoded = Path(target_path_decoded_str)
                
                if not target_path_decoded.exists():
                    file_errors.append(f"Broken Image: {img} (resolved: {target_path_str})")

        if file_errors:
            report.append(f"\n📄 {file_path.name}")
            for err in file_errors:
                report.append(f"  - {err}")
            total_errors += len(file_errors)

    if total_errors == 0:
        print("✅ No broken local links or images found!")
    else:
        print(f"❌ Found {total_errors} broken links/images in {len(html_files)} files.")
        print("\n".join(report))

if __name__ == "__main__":
    # Assuming script is run from root or scripts/ dir, adjust path
    # based on user info: c:\Users\sounn\Git\gis\
    base_dir = Path(r"c:\Users\sounn\Git\gis\chapters")
    check_chapters(base_dir)
