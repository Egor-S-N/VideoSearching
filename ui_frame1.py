# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PythonProjects\VideoSearching\frame1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choise_video_btn = QtWidgets.QPushButton(self.centralwidget)
        self.choise_video_btn.setGeometry(QtCore.QRect(20, 90, 125, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choise_video_btn.setFont(font)
        self.choise_video_btn.setObjectName("choise_video_btn")
        self.video_path = QtWidgets.QLineEdit(self.centralwidget)
        self.video_path.setEnabled(False)
        self.video_path.setGeometry(QtCore.QRect(20, 50, 331, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.video_path.setFont(font)
        self.video_path.setObjectName("video_path")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 119, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.image_path = QtWidgets.QLineEdit(self.centralwidget)
        self.image_path.setEnabled(False)
        self.image_path.setGeometry(QtCore.QRect(20, 320, 331, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.image_path.setFont(font)
        self.image_path.setObjectName("image_path")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 126, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.choose_image_btn = QtWidgets.QPushButton(self.centralwidget)
        self.choose_image_btn.setGeometry(QtCore.QRect(20, 360, 132, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_image_btn.setFont(font)
        self.choose_image_btn.setObjectName("choose_image_btn")
        self.show_image = QtWidgets.QLabel(self.centralwidget)
        self.show_image.setGeometry(QtCore.QRect(360, 300, 451, 251))
        self.show_image.setAutoFillBackground(True)
        self.show_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.show_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.show_image.setText("")
        self.show_image.setObjectName("show_image")
        self.video_widget = QtWidgets.QWidget(self.centralwidget)
        self.video_widget.setGeometry(QtCore.QRect(360, 10, 451, 251))
        self.video_widget.setAutoFillBackground(True)
        self.video_widget.setObjectName("video_widget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 560, 142, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.but_execute = QtWidgets.QPushButton(self.layoutWidget)
        self.but_execute.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_execute.setFont(font)
        self.but_execute.setObjectName("but_execute")
        self.horizontalLayout.addWidget(self.but_execute)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setEnabled(True)
        self.play_btn.setGeometry(QtCore.QRect(360, 267, 93, 28))
        self.play_btn.setObjectName("play_btn")
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setEnabled(True)
        self.pause_btn.setGeometry(QtCore.QRect(459, 267, 93, 28))
        self.pause_btn.setObjectName("pause_btn")
        self.restart_btn = QtWidgets.QPushButton(self.centralwidget)
        self.restart_btn.setGeometry(QtCore.QRect(558, 267, 93, 28))
        self.restart_btn.setObjectName("restart_btn")
        self.cb_input = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_input.setGeometry(QtCore.QRect(20, 160, 139, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_input.setFont(font)
        self.cb_input.setObjectName("cb_input")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video finding alghoritm"))
        self.choise_video_btn.setText(_translate("MainWindow", "choose video"))
        self.label.setText(_translate("MainWindow", "Choose video"))
        self.label_2.setText(_translate("MainWindow", "Choose image"))
        self.choose_image_btn.setText(_translate("MainWindow", "choose image"))
        self.but_execute.setText(_translate("MainWindow", "Execute"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.pause_btn.setText(_translate("MainWindow", "Pause"))
        self.restart_btn.setText(_translate("MainWindow", "Replay"))
        self.cb_input.setText(_translate("MainWindow", "use camera?"))
