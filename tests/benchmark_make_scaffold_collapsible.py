import time
import re
import os
import glob
import sys

# Read a few files
files = glob.glob('chapters/*.html')
if not files:
    print("No files found!")
    sys.exit(1)

contents = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        contents.append(file.read())

print(f"Loaded {len(contents)} files for benchmarking.")

# Baseline: compile inside loop
def run_baseline(iterations=1000):
    start = time.time()
    for _ in range(iterations):
        for content in contents:
            section_pattern = re.compile(r'(<section\s+class=["\']card\s+learning-scaffold["\'][^>]*>)', re.IGNORECASE)
            match_section = section_pattern.search(content)

            if match_section:
                head_pattern = re.compile(r'(<div\s+class=["\']scaffold-head["\'][^>]*>)', re.IGNORECASE)
                match_head = head_pattern.search(content)

                # dynamic tag compilation
                tag_name = 'section'
                p = re.compile(r'(</?'+tag_name+r'\b[^>]*>)', re.IGNORECASE)
                list(p.finditer(content[:1000])) # just to do something
    return time.time() - start

# Optimized: compile outside loop
SECTION_PATTERN = re.compile(r'(<section\s+class=["\']card\s+learning-scaffold["\'][^>]*>)', re.IGNORECASE)
HEAD_PATTERN = re.compile(r'(<div\s+class=["\']scaffold-head["\'][^>]*>)', re.IGNORECASE)
TAG_RE_CACHE = {}

def get_tag_pattern(tag_name):
    if tag_name not in TAG_RE_CACHE:
        TAG_RE_CACHE[tag_name] = re.compile(r'(</?'+tag_name+r'\b[^>]*>)', re.IGNORECASE)
    return TAG_RE_CACHE[tag_name]

def run_optimized(iterations=1000):
    start = time.time()
    for _ in range(iterations):
        for content in contents:
            match_section = SECTION_PATTERN.search(content)

            if match_section:
                match_head = HEAD_PATTERN.search(content)

                p = get_tag_pattern('section')
                list(p.finditer(content[:1000]))
    return time.time() - start

baseline_time = run_baseline(1000)
optimized_time = run_optimized(1000)

print(f"Baseline Time:  {baseline_time:.4f} seconds")
print(f"Optimized Time: {optimized_time:.4f} seconds")
print(f"Improvement:    {(baseline_time - optimized_time) / baseline_time * 100:.2f}%")
