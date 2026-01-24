import unittest
import glob
import os

class TestPlaceholders(unittest.TestCase):
    def test_no_todos_in_chapters(self):
        # Find all chapter HTML files
        chapter_files = glob.glob(os.path.join('chapters', 'chapter-*.html'))

        found_todos = []

        for filepath in chapter_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if '<!-- TODO -->' in content:
                    found_todos.append(filepath)

        # Fail if any TODOs were found
        if found_todos:
            self.fail(f"Found unresolved '<!-- TODO -->' markers in the following chapters: {', '.join(found_todos)}")

if __name__ == '__main__':
    unittest.main()
