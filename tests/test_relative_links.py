import os
import unittest
import re

class TestLinks(unittest.TestCase):
    def test_no_ims_placeholders(self):
        placeholders = ['$IMS-CC-FILEBASE$', '$IMS-CC-FILEBASE$'] 
        
        for root, dirs, files in os.walk('.'):
            if 'conductor' in root or '.git' in root or 'tests' in root or 'scripts' in root or 'references' in root:
                continue
            for file in files:
                if file.endswith('.html') or file.endswith('.css'):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for p in placeholders:
                            if p in content:
                                self.fail(f"Found placeholder {p} in {path}")

    def test_no_absolute_paths(self):
        # Regex for src="/..." or href="/..."
        # But allow http://, https://, //
        regex = re.compile(r'(src|href)=["\']/(?!(/))')
        
        for root, dirs, files in os.walk('.'):
            if 'conductor' in root or '.git' in root or 'tests' in root or 'scripts' in root or 'references' in root:
                continue
            for file in files:
                if file.endswith('.html'):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = regex.findall(content)
                        if matches:
                            self.fail(f"Found absolute path in {path}")

if __name__ == '__main__':
    unittest.main()
