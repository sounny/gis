import os
import re
from pathlib import Path
from urllib.parse import unquote
from concurrent.futures import ThreadPoolExecutor

def check_file_links(args):
    """
    Helper function to check links in a single file.
    args is a tuple: (file_path, root_path, link_pattern, img_pattern)
    """
    file_path, root_path, link_pattern, img_pattern = args
    file_broken_links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check links
        links = link_pattern.findall(content)
        for link in links:
            if not link or link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
                continue

            # Handle anchors and query params in file paths
            link_clean = link.split('#')[0].split('?')[0]
            if not link_clean:
                continue

            target_path = (file_path.parent / link_clean).resolve()
            if not target_path.exists():
                # Try unquoting
                decoded_link = unquote(link_clean)
                target_path_decoded = (file_path.parent / decoded_link).resolve()
                if not target_path_decoded.exists():
                    file_broken_links.append(f"Broken Link: {link} (resolved: {target_path})")

        # Check images
        images = img_pattern.findall(content)
        for img in images:
            if not img or img.startswith(('http://', 'https://', 'data:')):
                continue

            img_clean = img.split('?')[0]
            target_path = (file_path.parent / img_clean).resolve()
            if not target_path.exists():
                # Try unquoting
                decoded_img = unquote(img_clean)
                target_path_decoded = (file_path.parent / decoded_img).resolve()
                if not target_path_decoded.exists():
                    file_broken_links.append(f"Broken Image: {img} (resolved: {target_path})")

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

    if file_broken_links:
        return (file_path.name, file_broken_links)
    return None

def check_chapters(chapters_dir):
    chapters_path = Path(chapters_dir)
    html_files = sorted(list(chapters_path.glob("*.html")))
    root_path = chapters_path.parent
    
    print(f"Checking {len(html_files)} chapters in {chapters_path}...")

    link_pattern = re.compile(r'href=["\'](.*?)["\']')
    img_pattern = re.compile(r'src=["\'](.*?)["\']')

    args_list = [(f, root_path, link_pattern, img_pattern) for f in html_files]

    all_broken_links = []
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(check_file_links, args_list)
        for res in results:
            if res:
                all_broken_links.append(res)

    total_errors = sum(len(links) for _, links in all_broken_links)

    if total_errors == 0:
        print("[SUCCESS] No broken local links or images found!")
    else:
        print(f"[ERROR] Found {total_errors} broken links/images in {len(html_files)} files.")
        for filename, errors in all_broken_links:
            print(f"\n[FILE] {filename}")
            for err in errors:
                print(f"  - {err}")

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent / "chapters"
    check_chapters(base_dir)
