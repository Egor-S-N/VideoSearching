import cv2, kivy
from kivy.app import App
from kivy.uix.video import Video


def test():
    return ('Sources/forest1080.mp4')
def show_video():
    video = cv2.VideoCapture('Sources/forest1080.mp4')
    while(video.isOpened()):
        ret, frame = video.read()
        cv2.imshow('test', frame)
        print(video.get(5))
        if cv2.waitKey(1) == ord('q'):
            break



class MainApp(App):
    def build(self):
        video = Video(source = 'Sources/forest1080.mp4')
        video.state = "play"
        video.options = {'eos':'loop'}
        video.allow_stretch = True
        

        return video

        

if __name__ == "__main__":
    app = MainApp()
    app.run()