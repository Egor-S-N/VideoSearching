from kivy.uix.boxlayout import BoxLayout
from tkinter import filedialog


def choose_file() -> str:
    """Open file dialog and choose file"""
    file_source = filedialog.askopenfilename()
    if file_source != "":
        return file_source


class MainWindow(BoxLayout):
    def __init__(self, **kwargs) -> None:
        """Constructor"""
        super().__init__(**kwargs)
        self._video_source = None
        self._photo_source = None

    def choose_video_click(self) -> None:
        """fill video source"""
        self.ids.main_video.source = choose_file()

    def choose_image_click(self) -> None:
        """fill image source"""
        self.ids.searching_image.source = choose_file()

#
# def test():
#     video = VideoPlayer(source='Sources/forest1080.mp4')
#     video.state = "play"
#     video.options = {'eos': 'loop'}
#     video.allow_stretch = True
#     return video
