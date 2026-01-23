import os
import unittest

class TestStructure(unittest.TestCase):
    def test_no_manifest(self):
        self.assertFalse(os.path.exists('imsmanifest.xml'), 'imsmanifest.xml should have been removed')

if __name__ == '__main__':
    unittest.main()