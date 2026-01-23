import os
import shutil
import json

SOURCE_DIR = 'references/uf_canvas_extract'
DEST_DIR = 'assets/img'
EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

mapping = {}

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in EXTENSIONS:
            src_path = os.path.join(root, file)
            
            # Construct new name to avoid collisions
            new_name = file
            counter = 1
            # Check if file exists in dest (collision)
            # BUT ALSO check if we already moved a file with this name (unlikely since we move source)
            # Actually, shutil.move deletes the source.
            
            while os.path.exists(os.path.join(DEST_DIR, new_name)):
                name_part, ext_part = os.path.splitext(file)
                new_name = f"{name_part}_{counter}{ext_part}"
                counter += 1
            
            dest_path = os.path.join(DEST_DIR, new_name)
            try:
                shutil.move(src_path, dest_path)
                mapping[src_path] = dest_path
                # print(f"Moved {src_path} -> {dest_path}")
            except Exception as e:
                print(f"Error moving {src_path}: {e}")

# Save mapping for future reference (e.g. link updating)
# We use forward slashes for portability in the JSON
clean_mapping = {k.replace('\\', '/'): v.replace('\\', '/') for k, v in mapping.items()}

with open('conductor/asset_mapping.json', 'w') as f:
    json.dump(clean_mapping, f, indent=2)

print(f"Moved {len(mapping)} images.")
