import unittest
import os
import shutil
from Library import Library



class TestLibrary(unittest.TestCase):
    

    def setUp(self):
        self.library = Library()

    def test_video_source(self):
        self.library.video_source = "Sources\VERT_TEST.mkv"
        self.assertEqual(self.library.video_source, "Sources\VERT_TEST.mkv")

    def test_image_source(self):
        self.library.image_source = "Sources\search_vert.png"
        self.assertEqual(self.library.image_source, "Sources\search_vert.png")

    def test_show_video(self):
        self.library.video_source = "D:\PythonProjects\VideoSearching\Sources\VERT_TEST.mkv"
        self.library.image_source = "D:\PythonProjects\VideoSearching\Sources\search_vert.png"
        self.library.show_video()
        self.assertTrue(os.path.exists("test_0.png"))
    @classmethod  
    def tearDownClass(cls):
        for file in os.listdir(os.getcwd()):
                shutil.rmtree(file)

if __name__ == '__main__':
    unittest.main()
