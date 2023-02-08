import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from Library import Library

qtcreator_file = "frame1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._Library = Library
        self.video_path.textChanged[str].connect(self.on_text_changed)
        self.image_path.textChanged[str].connect(self.on_text_changed)
        self.choose_image_btn.clicked.connect(self.choose_image_click)
        self.choise_video_btn.clicked.connect(self.choose_video_click)

    def choose_image_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', None, "Image (*.png *.jpg *jpeg)")
        if file_path != "":
            self._Library.video_source = file_path
            self.image_path.setText(file_path)
            self.show_image.setPixmap(QPixmap(file_path))

    def choose_video_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', None, "Image (*.mp4 *.avi *mov)")
        if file_path != "":
            self._Library.image_source = file_path
            self.video_path.setText(file_path)

    def on_text_changed(self, text):
        if (self.video_path.text() != "") and (self.image_path.text() != ""):
            self.but_execute.setEnabled(True)
        else:
            self.but_execute.setEnabled(False)


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
