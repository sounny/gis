import os
import re
from pathlib import Path

def fix_links(root_dir):
    root_path = Path(root_dir)
    chapters_dir = root_path / "chapters"
    
    # Replacement rules
    replacements = [
        (r'assets/images/', 'assets/img/'),
        (r'vector_gis_components.png', 'raster_vs_vector_simple.png'), # Best guess replacement
        # (r'manual_digitizing_tablet.png', '???'), # No obvious replacement found
    ]
    
    for file_path in chapters_dir.glob("*.html"):
        try:
            # Read with utf-8, ignore errors to handle any weird chars temporarily
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            for old, new in replacements:
                content = content.replace(old, new)
            
            if content != original_content:
                print(f"Fixed links in {file_path.name}")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Fixing links in {current_dir}...")
    fix_links(current_dir)
