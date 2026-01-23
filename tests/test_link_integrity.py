import os
import unittest
from urllib.parse import urlparse

class TestLinkIntegrity(unittest.TestCase):
    def test_local_links_exist(self):
        """Check if all local href and src links point to existing files."""
        all_broken_links = {}
        for root, dirs, files in os.walk('.'):
            # Skip some directories
            if any(skip in root for skip in ['conductor', '.git', 'tests', 'scripts', 'references']):
                continue
            
            for file in files:
                if not file.endswith('.html'):
                    continue
                
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Simple regex-based extraction
                import re
                links = re.findall(r'(?:href|src)=["\'](.*?)["\']', content)
                
                broken_links = []
                for link in links:
                    # Skip external links
                    if link.startswith('http') or link.startswith('//') or link.startswith('data:') or link.startswith('#'):
                        continue
                    
                    # Parse link to remove query params or fragments
                    link_path = urlparse(link).path
                    if not link_path:
                        continue
                        
                    # Resolve path relative to the current file
                    target_path = os.path.normpath(os.path.join(root, link_path))
                    
                    if not os.path.exists(target_path):
                        broken_links.append(f"{link} (Resolved to: {target_path})")
                
                if broken_links:
                    all_broken_links[path] = broken_links
        
        if all_broken_links:
            msg = "Found broken links:\n"
            for path, links in all_broken_links.items():
                msg += f"  {path}:\n"
                for link in links:
                    msg += f"    - {link}\n"
            self.fail(msg)

if __name__ == '__main__':
    unittest.main()

