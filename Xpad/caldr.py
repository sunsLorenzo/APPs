#!/usr/bin/python3
#coding: utf-8
import os.path, time, sys, threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  


class Xpad(QWidget):
	def __init__(self):
		super().__init__()
# 		self.setWindowFlags(Qt.SplashScreen)#取消标题栏和边框
# 		self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
		for i in range(1,8):
			pass
		self.txt = QTextEdit()
		self.palette1 = QPalette()
		self._padding = 5
		try:
			self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('green.png')))   
			self.setPalette(self.palette1)#set palette to draw the background
			# self.txt.setPalette(self.palette1)
		except Exception as e:
			print('setting bg failed')


# 		self.setWindowFlags(Qt.FramelessWindowHint )   #################无标题栏
		# self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
		self.label = QLabel()
		self.label.setFont(QFont("Timers",12,QFont.Bold))
		self.txt.setFont(QFont("Timers",9,))
		self.label.setStyleSheet("background-color:rgb(156,245,186)")
		# with open('setColor.txt', 'r') as c:
		#
		# 	self.label.setStyleSheet("background-color:rgb"+c.read())

		# start time showing  thread
		self.thd = threading.Thread(target=self.show_time, name='LoopThread')
		self.thd.start()
		self.initGUI()



	def initGUI(self):
		h_box = QHBoxLayout()
		v_box = QVBoxLayout()
		v_box.addWidget(self.label)
		v_box.addWidget(self.txt)
		

		self.setLayout(v_box)
		self.setGeometry(1600, 0, 241, 400)
		# with open('setGeometry.txt', 'r') as h:
		# 	a = h.readline()[19:-1]
		# 	a = list(a.split(','))
		# 	print(a)
		# 	self.setGeometry(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
		self.setWindowTitle('Xpad')

		# self.setWindowFlags(Qt.WindowMinimizeButtonHint) #设置为不能最大化
		# self.setFixedSize(self.width(), self.height())  #  size fixed
		
		self.txt.setStyleSheet("background-color:rgb(156,245,186)")
		# with open('setColor.txt', 'r') as c:
		#
		# 	self.txt.setStyleSheet("background-color:rgb"+c.read())


		with open('XpadText.txt', 'r') as f:
			self.txt.setText(f.read())				####读文件
		
		try:
			self.setWindowIcon(QIcon('icon.png'))#  set icon
		except Exception as e:
			print('setting icon failed')

		self.show()


	def show_time(self):
		while True:
			# print('update time')
			a = time.strftime('%B-%d-%A \n\n%H:%M:%S')
			self.label.setText(a)
			time.sleep(0.3)

##################################实现移动窗体:############################################
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QApplication.postEvent(self, QEvent(174))
			event.accept()
			with open('setGeometry.txt', 'w') as h:
				h.write(str(self.frameGeometry()))
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

##############################################################################
	def enterEvent(self, event):


		print("enter")

	def leaveEvent (self, event):
		# self.setWindowFlags(Qt.SplashScreen)#取消标题栏
		# self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
		# self.setWindowFlags(Qt.WindowMinimizeButtonHint)
		print("out&saving")
		####save the text into file 
		with open('XpadText.txt', 'w') as f:
			f.write(self.txt.toPlainText())      #写文件

	
app = QApplication(sys.argv)
pad = Xpad()
sys.exit(app.exec_())