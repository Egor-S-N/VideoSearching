# import cv2
# from kivy.app import App
# from mainWindow import MainWindow
# from kivy.core.window import Window
import sys
from PyQt5 import QtWidgets, uic

qtcreator_file  = "frame1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.choise_video_btn.clicked.connect(self.printing)

    
    def printing(self):
        print("asd")



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


# class App(App):
#     def build(self):
#         Window.size = (800, 700)
#         return MainWindow()



# if __name__ == "__main__":
#     App().run()
