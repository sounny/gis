import os
import re
import urllib.parse
from pathlib import Path

def check_links(root_dir):
    root_path = Path(root_dir)
    chapters_dir = root_path / "chapters"
    
    # Regex for finding links
    link_pattern = re.compile(r'(?:href|src)=["\'](.*?)["\']')
    
    broken_links = []
    
    # Walk through chapters
    for file_path in chapters_dir.glob("*.html"):
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
                    broken_links.append({
                        'source': file_path.name,
                        'target': link,
                        'resolved': str(target_path_obj)
                    })
                    
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

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
