import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Library import Library

qtcreator_file = "frame1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(843, 622)
        self._Library = Library()
        self.videoOutput = self.makeVideoWidget()
        self.mediaPlayer = self.makeMediaPlayer()
        self.mediaPlayer.setVolume(0)

        self.video_path.textChanged[str].connect(self.on_text_changed)
        self.image_path.textChanged[str].connect(self.on_text_changed)

        self.choose_image_btn.clicked.connect(self.choose_image_click)
        self.choise_video_btn.clicked.connect(self.choose_video_click)

        self.but_execute.clicked.connect(self.but_execute_click)

    def makeMediaPlayer(self):
        mediaPlayer = QMediaPlayer()
        mediaPlayer.setVideoOutput(self.videoOutput)
        return mediaPlayer

    def makeVideoWidget(self):
        videoOutput = QVideoWidget(self)
        vbox = QVBoxLayout()
        vbox.addWidget(videoOutput)
        self.video_widget.setLayout(vbox)
        return videoOutput

    def choose_image_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', None, "Image (*.png *.jpg *jpeg)")
        if file_path != "":
            self._Library.image_source = file_path

            self.image_path.setText(file_path)
            self.show_image.setPixmap(QPixmap(file_path))

    def choose_video_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', None, "Video (*.mp4 *.avi *.mov *.mkv)")
        if file_path != "":
            self._Library.video_source = file_path

            print(self._Library.video_source)
            self.video_path.setText(file_path)

            self.mediaPlayer.setMedia(QMediaContent(QUrl(file_path)))
            self.mediaPlayer.play()

    def on_text_changed(self, text):
        if (self.video_path.text() != "") and (self.image_path.text() != ""):
            self.but_execute.setEnabled(True)
        else:
            self.but_execute.setEnabled(False)

    def but_execute_click(self):
        self._Library.show_video()


# create second fuct for textChandeg
# insert in 2 func try exepct 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

# # def show_video():
# #     video = cv2.VideoCapture(source='Sources/forest1080.mp4')
# #     while video.isOpened():
# #         ret, frame = video.read()
# #         cv2.imshow('test', frame)
# #         print(video.get(5))
# #         if cv2.waitKey(1) == ord('q'):
# #             break
