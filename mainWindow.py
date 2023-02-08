from kivy.uix.boxlayout import BoxLayout
from tkinter import filedialog


class MainWindow(BoxLayout):
    def __init__(self, **kwargs) -> None:
        """Constructor"""
        super().__init__(**kwargs)

    def choose_video_click(self) -> None:
        """Comment"""
        folder = filedialog.askopenfilename()
        if folder != "":
            print(folder)
            # self.ids.searching_image.source = folder
            self.ids.main_video.source = folder

#
# def test():
#     video = VideoPlayer(source='Sources/forest1080.mp4')
#     video.state = "play"
#     video.options = {'eos': 'loop'}
#     video.allow_stretch = True
#     return video
