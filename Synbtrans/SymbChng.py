#!/usr/bin/python3
#coding: utf-8
import os.path, time, sys, threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Xpad(QWidget):
    def __init__(self):
        super().__init__()


        self.flag = 1
        # self.setStyleSheet("background-image:url(bgbg.png)")
        # self.setWindowFlags(Qt.SplashScreen)#取消标题栏和边框
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
        self.txt = QTextEdit()
        self.palette1 = QPalette()
        self.padding = 0
        # try:
        #     self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('green.png')))
        #     self.setPalette(self.palette1)#set palette to draw the background
        #     # self.txt.setPalette(self.palette1)
        # except Exception as e:
        #     print('setting bg failed')

        # self.setWindowFlags(Qt.FramelessWindowHint )   #################无标题栏
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.txtout = QTextEdit()
        self.txt.setFont(QFont("Timers",10))
        self.txtout.setFont(QFont("Timers",10,))
        # self.txt.setStyleSheet("color: rgb(255,255,255) ")

        # self.txt.setStyleSheet("background-image:url(bgbg.png)")
        # self.label.setStyleSheet("background-color:rgb(211,211,211)")
        self.setStyleSheet("background-color:rgb(211,211,211)")
        self.button1 = QPushButton("enter2space")
        self.button2 = QPushButton("comma2tab")
        self.button3 = QPushButton("tab2comma")


        self.initGUI()



    def initGUI(self):
        h_box1 =QHBoxLayout()
        h_box1.addWidget(self.txt)
        h_box1.addWidget(self.txtout)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.button1)
        h_box2.addWidget(self.button2)
        h_box2.addWidget(self.button3)


        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)

        self.setGeometry(600, 0, 700, 600)
        try:
            self.setWindowIcon(QIcon('icon.png'))#  set icon
        except Exception as e:
            print('setting icon failed')

        self.button1.clicked.connect(self.enter2space)
        self.button2.clicked.connect(self.comma2tab)
        self.button3.clicked.connect(self.tab2comma)
        self.show()

    def enter2space(self):
        text = self.txt.toPlainText()
        text = text.replace("\n"," ")
        text = text.replace(". ",".\n")
        text = text.replace("Fig.\n","Fig. ")
        self.txtout.setText(text)

    def comma2tab(self):
        text = self.txt.toPlainText()
        text = text.replace(",","\t")
        self.txtout.setText(text)
    def tab2comma(self):
        text = self.txt.toPlainText()
        text = text.replace("\t",",")
        self.txtout.setText(text)


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()




app = QApplication(sys.argv)
pad = Xpad()
sys.exit(app.exec_())