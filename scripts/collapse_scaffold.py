import glob
import os

files = glob.glob(os.path.join('c:\\Users\\sounn\\Git\\gis\\chapters', '*.html'))
print(f"Found {len(files)} files.")

target_string = '<details class="learning-scaffold-details" open>'
replacement_string = '<details class="learning-scaffold-details">'

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_string in content:
            new_content = content.replace(target_string, replacement_string)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
        else:
            print(f"No match in {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Batch collapse complete.")
