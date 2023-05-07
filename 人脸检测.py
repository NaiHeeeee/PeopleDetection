import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from keras.models import load_model
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 451))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 10, 581, 451))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 560, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 560, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 570, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(850, 550, 221, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("color: red; font-size: 38pt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 490, 101, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 490, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理：人数检测"))
        self.label.setText(_translate("MainWindow", "原图"))
        self.label_2.setText(_translate("MainWindow", "检测后"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "人数检测"))
        self.label_3.setText(_translate("MainWindow", "人数："))
        self.label_4.setText(_translate("MainWindow", "图片所在路径："))
        self.pushButton.clicked.connect(self.display_orginal)
        self.pushButton_2.clicked.connect(self.pepple_detection)

    def display_orginal(self):
        self.cwd = os.getcwd()
        filename = QFileDialog.getOpenFileName(self, "选取要检测的图片", self.cwd, "Image Files (*.jpg)")
        if filename[0] == "":
            print("\n取消选择")
            return
        self.lineEdit.setText(filename[0])
        if os.path.isfile(self.lineEdit.text()) == True:

            JPG = QtGui.QPixmap(self.lineEdit.text())
            self.label.setPixmap(JPG)
            self.label.setScaledContents(True)
        else:
            pass

    # def display_processed(self, img):
    #     # 将 OpenCV 图片格式转换为 QImage 格式
    #     height, width, channel = img.shape
    #     bytesPerLine = channel * width
    #     qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    #
    #     # 将 QImage 显示在 QLabel 控件中
    #     self.label.setPixmap(QPixmap.fromImage(qImg))
    #     self.label.setScaledContents(True)

    def pepple_detection(self):
        # 加载人脸检测模型
        face_detection_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # 加载人脸识别模型
        face_recognition_model = load_model('model/face_detection_model.h5')

        # 加载图片
        img = cv2.imread(self.lineEdit.text())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 检测人脸
        faces = face_detection_model.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

        # 统计人脸数
        count = len(faces)

        self.textBrowser.setText(str(count))
        # 遍历每张人脸
        for (x, y, w, h) in faces:
            # 提取人脸部分图片
            face = img[y:y + h, x:x + w]

            # 预处理图片
            face = cv2.resize(face, (224, 224))
            face = face.astype('float32') / 255.0
            face = np.expand_dims(face, axis=0)

            # 使用模型预测人脸数量
            count = int(face_recognition_model.predict(face)[0][0])

            # 在人脸部分画框
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        qImg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qImg.copy())
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
