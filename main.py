import sys
from Library import Library
import cv2
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QFileDialog

qtcreator_file = "window.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """application constructor"""
        self.isCamera = False
        self.isVideo = False
        self.isImage = False

        self.camera_index = None

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self._Library = Library()
        self.setupUi(self)
        self.load_cameras()
        self.camera_list.clicked.connect(self.item_clicked)
        self.rb_from_video.toggled.connect(self.onChangeInput)
        self.rb_from_camera.toggled.connect(self.onChangeInput)

        self.image_preview.mousePressEvent = self.onImageClick

        self.choose_image_btn.clicked.connect(self.chooseImageClick)

        self.choose_video_btn.clicked.connect(self.chooseVideoClick)

        self.execute_btn.clicked.connect(self.start_searching_click)

        self.cap = cv2.VideoCapture()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

    def chooseImageClick(self) -> None:
        """Method for choising image from user`s computer"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open file', None, "Image (*.png *.jpg *jpeg)")
        if file_path != "":
            self._Library.image_source = file_path
            self.image_preview.setPixmap(QPixmap(file_path))
            self.isImage = True
            self.check_video_image()

    def chooseVideoClick(self) -> None:
        '''Method for choising video from user`s computer'''
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open file', None, "Video (*.mp4 *.avi *.mov *.mkv)")
        if file_path != "":
            self._Library.video_source = file_path
            self.timer.stop()
            self.cap.release()
            self.cap = cv2.VideoCapture(file_path)
            self.timer.start()
            self.isVideo = True
            self.isCamera = False
            self.check_video_image()

    def onImageClick(self, event) -> None:
        """Scale image to specified dimensions"""
        print('image was clicked')

    def onChangeInput(self) -> None:
        """Change video input (video / camera)"""
        if self.rb_from_video.isChecked():
            self.choose_video_btn.setMaximumHeight(30)
            self.camera_list.setMaximumHeight(0)
        elif self.rb_from_camera.isChecked():
            self.choose_video_btn.setMaximumHeight(0)
            self.camera_list.setMaximumHeight(100)

    def load_cameras(self) -> None:
        """Method to display all connected cameras"""
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
            dev_port += 1

            self.model = QStandardItemModel()
            self.camera_list.setModel(self.model)

            for i in working_ports:
                item = QStandardItem(str(i))
                self.model.appendRow(item)

    def item_clicked(self, index) -> None:
        """Method to select available camera"""
        item = self.model.itemFromIndex(index)
        item = int(item.text())
        self.timer.stop()
        self.cap.release()
        self.cap = cv2.VideoCapture(item)
        self.isCamera = True
        self.isVideo = False
        self.camera_index = item 
        self.timer.start()
        self.check_video_image()

    def update_frame(self) -> None:
        """Method for refreshing preview window frames"""
        ret, frame = self.cap.read()
        if ret:
            image = QImage(
                frame, frame.shape[1], frame.shape[0], QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(image)
            self.video_preview.setPixmap(pixmap)
        else:
            self.cap.release()

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

    def check_video_image(self) -> None:
        """Checking if video and image or camera and image are full"""
        if (self.isVideo or self.isCamera) and self.isImage:
            self.execute_btn.setEnabled(True)
        else:
            self.execute_btn.setEnabled(False)


    def start_searching_click(self) -> None:
        """Method for launching the object search algorithm"""
        # print(f"Camera: {self.isCamera} \nVideo: {self.isVideo} \nImage: {self.isImage}")
        # print(f"CameraIndex: {self.camera_index}")
        self.cap = cv2.VideoCapture()
        self.timer.stop()
        if self.isCamera:
            self._Library.search_in_camera(self.camera_index)
            self.cap = cv2.VideoCapture(self.camera_index)
            self.timer.start()
            
        elif self.isVideo:
            self._Library.search_in_video()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
