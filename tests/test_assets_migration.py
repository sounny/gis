import os
import unittest

class TestAssetsMigration(unittest.TestCase):
    def test_images_moved(self):
        source_dir = 'references/uf_canvas_extract'
        extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        
        found_media = []
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    found_media.append(os.path.join(root, file))
        
        self.assertEqual(len(found_media), 0, f"Found {len(found_media)} images remaining in {source_dir}. Example: {found_media[:3]}")

    def test_destination_populated(self):
        dest_dir = 'assets/img'
        extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        found_dest = []
        if os.path.exists(dest_dir):
            for root, dirs, files in os.walk(dest_dir):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in extensions:
                        found_dest.append(os.path.join(root, file))
        
        self.assertGreater(len(found_dest), 0, "assets/img should contain moved images")

if __name__ == '__main__':
    unittest.main()