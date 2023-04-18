# import sys
# from PyQt5 import QtWidgets, uic
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import *
# from PyQt5.QtMultimedia import *
# from PyQt5.QtMultimediaWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from Library import Library

# qtcreator_file = "frame1.ui"
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


# class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         QtWidgets.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)
#         self.setFixedSize(843, 622)
#         self._Library = Library()
#         self.videoOutput = self.makeVideoWidget()
#         self.mediaPlayer = self.makeMediaPlayer()
#         self.mediaPlayer.setVolume(0)

#         self.cb_input.stateChanged.connect(self.cb_input_is_checked)

#         self.play_btn.setVisible(False)
#         self.pause_btn.setVisible(False)
#         self.restart_btn.setVisible(False)

#         self.play_btn.clicked.connect(self.play_btn_click)
#         self.pause_btn.clicked.connect(self.pause_btn_click)
#         self.restart_btn.clicked.connect(self.replay_btn_click)

#         self.video_path.textChanged[str].connect(self.on_text_changed)
#         self.image_path.textChanged[str].connect(self.on_text_changed)

#         self.choose_image_btn.clicked.connect(self.choose_image_click)
#         self.choise_video_btn.clicked.connect(self.choose_video_click)

#         self.but_execute.clicked.connect(self.but_execute_click)

#     def cb_input_is_checked(self):
#         if self.cb_input.isChecked():
#             self.video_path.setText("")
#             self.mediaPlayer.setMedia(QMediaContent())
#             self.choise_video_btn.setEnabled(False)
#         else:
#              self.choise_video_btn.setEnabled(True)
            


#         if (self.cb_input.isChecked()) and (self.image_path.text() != ""):
#             self.but_execute.setEnabled(True)
#         else:
#             self.but_execute.setEnabled(False)

#     def makeMediaPlayer(self):
#         mediaPlayer = QMediaPlayer()
#         mediaPlayer.setVideoOutput(self.videoOutput)
#         return mediaPlayer

#     def makeVideoWidget(self):
#         videoOutput = QVideoWidget(self)
#         vbox = QVBoxLayout()
#         vbox.addWidget(videoOutput)
#         self.video_widget.setLayout(vbox)
#         return videoOutput

#     def choose_image_click(self):
#         file_path, _ = QFileDialog.getOpenFileName(
#             self, 'Open file', None, "Image (*.png *.jpg *jpeg)")
#         if file_path != "":
#             self._Library.image_source = file_path
#             print(file_path)
#             self.image_path.setText(file_path)
#             self.show_image.setPixmap(QPixmap(file_path))

#     def choose_video_click(self):
#         # file_path, _ = QFileDialog.getOpenFileName(
#         #     self, 'Open file', None, "Video (*.mp4 *.avi *.mov *.mkv)")
#         file_path = '/home/egor/Diplom/VideoSearching/Sources/video.mp4'
#         if file_path != "":
#             self._Library.video_source = file_path

#             self.video_path.setText(file_path)
#             print(file_path)
#             self.mediaPlayer.setMedia(QMediaContent(QUrl(file_path)))
#             self.mediaPlayer.play()
#             self.mediaPlayer.pause()
#             self.play_btn.setVisible(True)
#             self.pause_btn.setVisible(True)
#             self.restart_btn.setVisible(True)

#     def play_btn_click(self):
#         self.mediaPlayer.play()

#     def pause_btn_click(self):
#         self.mediaPlayer.pause()

#     def replay_btn_click(self):
#         self.mediaPlayer.stop()
#         self.mediaPlayer.play()

#     def on_text_changed(self, text):
#         if self.video_path.text() == "":
#             self.play_btn.setVisible(False)
#             self.pause_btn.setVisible(False)
#             self.restart_btn.setVisible(False)
#         else:
#             self.play_btn.setVisible(True)
#             self.pause_btn.setVisible(True)
#             self.restart_btn.setVisible(True)

#         if (self.video_path.text() != "" or self.cb_input.isChecked()) and (self.image_path.text() != ""):
#             self.but_execute.setEnabled(True)
#         else:
#             self.but_execute.setEnabled(False)

#     def but_execute_click(self):
#         if self.cb_input.isChecked():
#             self._Library.search_in_camera()
#         else:
#             self._Library.search_in_video()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())





import sys

import cv2
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QTimer, QModelIndex
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

qtcreator_file = "window.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class VideoPlayer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.load_cameras()
        self.camera_list.clicked.connect(self.item_clicked)
        self.rb_from_video.toggled.connect(self.onChangeInput)
        self.rb_from_camera.toggled.connect(self.onChangeInput)

        self.image_preview.mousePressEvent = self.onImageClick
     



        # # Create a label to display the video stream
        # self.label = QLabel(self)

        # # Create a vertical layout to hold the label
        # layout = QVBoxLayout()
        # layout.addWidget(self.label)
        # self.setLayout(layout)

        # # Initialize the video capture object
        # self.cap = cv2.VideoCapture(0)

        # # Start the video stream
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_frame)
        # self.timer.start(50)

    def onImageClick(self, event) -> None:
        """Scale image to specified dimensions"""
        print('sadlkas;ldkasd')




    def onChangeInput(self):
        if self.rb_from_video.isChecked():
            self.choose_video_btn.setMaximumHeight(30)
            self.camera_list.setMaximumHeight(0)
        elif self.rb_from_camera.isChecked():
            self.choose_video_btn.setMaximumHeight(0)
            self.camera_list.setMaximumHeight(100)



    def load_cameras(self):
           
        non_working_ports = []
        dev_port = 0
        working_ports = []
        while len(non_working_ports) < 6:
            camera = cv2.VideoCapture(dev_port)
            if not camera.isOpened():
                non_working_ports.append(dev_port)
            else:
                is_reading, img = camera.read()
                if is_reading:
                    working_ports.append(dev_port)
            dev_port +=1

            self.model = QStandardItemModel()
            self.camera_list.setModel(self.model)

            for i in working_ports:
                item = QStandardItem(str(i))
                self.model.appendRow(item)


    
    def item_clicked(self, index):
        item = self.model.itemFromIndex(index)
        print(f"Item clicked: {item.text()}")
       

    def update_frame(self):
        # Read a frame from the video stream
        ret, frame = self.cap.read()

        # Convert the frame to a QImage
        if ret:
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)

    def closeEvent(self, event):
        # Stop the video stream when the window is closed
        self.cap.release()
        self.timer.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
