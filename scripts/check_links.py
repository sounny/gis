import os
import re
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def check_file_links(args):
    """
    Helper function to check links in a single file.
    args is a tuple: (file_path, root_path, link_pattern)
    """
    file_path, root_path, link_pattern = args
    file_broken_links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = link_pattern.findall(content)

        for link in matches:
            # Skip anchors, empty links, and javascript:
            if not link or link.startswith('#') or link.startswith('javascript:') or link.startswith('mailto:'):
                continue

            # External links (just check format for now, could ping them but that's slow)
            if link.startswith('http://') or link.startswith('https://'):
                continue

            # Local links
            # Handle absolute paths from root (if any, though usually relative)
            if link.startswith('/'):
                target_path = root_path / link.lstrip('/')
            else:
                # Resolve relative path
                target_path = (file_path.parent / link).resolve()

            # Clean query params and anchors from local path
            target_path_str = str(target_path).split('?')[0].split('#')[0]
            target_path_obj = Path(target_path_str)

            if not target_path_obj.exists():
                file_broken_links.append({
                    'source': file_path.name,
                    'target': link,
                    'resolved': str(target_path_obj)
                })

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

    return file_broken_links

def check_links(root_dir):
    root_path = Path(root_dir)
    chapters_dir = root_path / "chapters"
    
    # Regex for finding links
    link_pattern = re.compile(r'(?:href|src)=["\'](.*?)["\']')
    
    files = list(chapters_dir.glob("*.html"))

    # Prepare arguments for each file
    args_list = [(f, root_path, link_pattern) for f in files]

    broken_links = []
    
    # Use ThreadPoolExecutor for parallel file processing
    # Adjust max_workers as needed, default is usually number of processors * 5
    with ThreadPoolExecutor() as executor:
        results = executor.map(check_file_links, args_list)
        for res in results:
            broken_links.extend(res)

    return broken_links

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Scanning for broken links in {current_dir}...")
    
    issues = check_links(current_dir)
    
    if issues:
        print(f"Found {len(issues)} broken links:")
        print("-" * 50)
        for issue in issues:
            print(f"File: {issue['source']}")
            print(f"  Link:   {issue['target']}")
            print(f"  Status: Missing")
            print("-" * 20)
    else:
        print("No broken local links found.")
