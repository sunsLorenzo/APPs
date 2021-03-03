#!/usr/bin/python3
import os.path, time, sys, threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  

class MyTime(QWidget):
	"""docstring for MyTime"""
	def __init__(self):
		super().__init__()
		
		self.label = QLabel("hello!!!")
		self.label.setFont(QFont("Timers",12,QFont.Bold))
		self.label.setStyleSheet("background-color:rgb(156,245,186)")

		# self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
		v_box=QVBoxLayout()
		v_box.addWidget(self.label)
		self.setLayout(v_box)
		self.show()

		



app = QApplication(sys.argv)
pad = MyTime()
sys.exit(app.exec_())