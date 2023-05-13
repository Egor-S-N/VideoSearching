import unittest
import os
import shutil
from Library import Library
import time


class TestLibrary(unittest.TestCase):
    

    def setUp(self):
        self.library = Library()

    def test_video_source(self):
        self.library.video_source = "Sources/clocks.mp4"
        self.assertEqual(self.library.video_source, "Sources/clocks.mp4")

    def test_image_source(self):
        self.library.image_source = "Sources/clock.png"
        self.assertEqual(self.library.image_source, "Sources/clock.png")

    def test_search_algorithm_with_image(self):
        self.library.image_source = "Sources/clock.png"
        self.library.video_source = "Sources/clocks.mp4"
        print(f"----------{self.library.image_source}-----------")
        self.library.search_algorithm_with_image(self.library.video_source)
        assert self.library._index > 0
    
    def test_search_algorithm_with_text(self):
        self.library = Library()
        time.sleep(1)
        self.library.video_source = "Sources/clocks.mp4"
        self.library.image_source = "Sources/clock.png"
        test_query = "clock"
        self.library.search_algorithm_with_text(query=test_query,value=self.library.video_source)
        assert self.library._index > 0

    @classmethod  
    def tearDownClass(cls):
        results_dir = os.path.join(os.getcwd(), "Results")
        for file in os.listdir(results_dir):
                full_path = os.path.join(results_dir, file)
                shutil.rmtree(full_path)

if __name__ == '__main__':
    unittest.main()
