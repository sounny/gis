import glob
import re
import os

# Pre-compile regex patterns for performance
SECTION_PATTERN = re.compile(r'(<section\s+class=["\']card\s+learning-scaffold["\'][^>]*>)', re.IGNORECASE)
HEAD_PATTERN = re.compile(r'(<div\s+class=["\']scaffold-head["\'][^>]*>)', re.IGNORECASE)
TAG_RE_CACHE = {}

def get_tag_pattern(tag_name):
    if tag_name not in TAG_RE_CACHE:
        TAG_RE_CACHE[tag_name] = re.compile(r'(</?'+tag_name+r'\b[^>]*>)', re.IGNORECASE)
    return TAG_RE_CACHE[tag_name]

# Use environment-portable relative path
files = glob.glob(os.path.join('chapters', '*.html'))
print(f"Found {len(files)} files.")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        match_section = SECTION_PATTERN.search(content)

        if not match_section:
            print(f"Skip: No scaffold in {os.path.basename(filepath)}")
            continue

        # Check if already processed
        if '<details class="learning-scaffold-details"' in content:
            print(f"Skip: Already processed {os.path.basename(filepath)}")
            continue

        print(f"Processing {os.path.basename(filepath)}...")
        
        # Helper to find closing tag
        def find_closing_tag(full_text, start_idx, tag_name):
            depth = 0
            # Matches </tag> or <tag ... >
            p = get_tag_pattern(tag_name)
            for m in p.finditer(full_text, start_idx):
                tag = m.group(1)
                is_close = tag.startswith('</')
                is_self_closing = tag.endswith('/>')
                
                if is_close:
                    depth -= 1
                elif not is_self_closing:
                    depth += 1
                
                if depth == 0:
                    return m.start(), m.end()
            return None, None

        # Find section end
        # Note: start_idx should be match_section.start() to count the opening tag itself as depth=1
        sec_close_start, sec_close_end = find_closing_tag(content, match_section.start(), 'section')
        if sec_close_start is None:
            print(f"Error: Could not find closing section for {os.path.basename(filepath)}")
            continue

        # Identify the content block limits
        inner_content = content[match_section.end():sec_close_start]
        inner_start_absolute = match_section.end()

        # Find scaffold-head div inside inner content
        match_head = HEAD_PATTERN.search(inner_content)
        
        if not match_head:
             print(f"Error: Could not find scaffold-head in {os.path.basename(filepath)}")
             continue

        # Calculate absolute start of head
        abs_head_start = inner_start_absolute + match_head.start()
        
        # Find where scaffold-head closes
        head_close_start, head_close_end = find_closing_tag(content, abs_head_start, 'div')
        
        if head_close_start is None:
             print(f"Error: Could not find closing div for head in {os.path.basename(filepath)}")
             continue

        # Construct new content replacement
        # Capture content before head (usually whitespace)
        pre_head_content = content[inner_start_absolute:abs_head_start]
        
        # Head content itself
        head_content = content[abs_head_start:head_close_end]
        
        # Rest of content
        rest_content = content[head_close_end:sec_close_start]
        
        # New structure
        # <details ... open>
        #   <summary> ... head ... </summary>
        #   ... rest ...
        # </details>
        
        new_inner = (
            f'{pre_head_content}'
            f'<details class="learning-scaffold-details" open>\n'
            f'  <summary>\n'
            f'{head_content}\n'
            f'  </summary>'
            f'{rest_content}'
            f'</details>'
        )

        final_content = content[:inner_start_absolute] + new_inner + content[sec_close_start:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
            
    except Exception as e:
        print(f"Critical Error processing {filepath}: {e}")

print("Batch processing complete.")
