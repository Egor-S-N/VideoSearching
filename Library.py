from tkinter import filedialog


class Library:
    def __init__(self):
        self._video_source = None
        self._image_source = None

    @property
    def video_source(self) -> str:
        return self._video_source

    @video_source.setter
    def video_source(self, value):
        self._video_source = value

    @property
    def image_source(self) -> str:
        return self._image_source

    @image_source.setter
    def image_source(self, value):
        self._image_source = value



# def test():
#     video = VideoPlayer(source='Sources/forest1080.mp4')
#     video.state = "play"
#     video.options = {'eos': 'loop'}
#     video.allow_stretch = True
#     return video
