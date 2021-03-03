#!/usr/bin/python3
#coding: utf-8
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time,threading
from multiprocessing import Process, Queue
import random
class Patatoaaa(QWidget):
	def __init__(self):
		super().__init__()
		self.q = Queue()

		self.sld = QSlider(Qt.Horizontal)
		self.b = QPushButton('START')
		self.l = QLabel('45')
		self.tm = QLabel('045:00')
		self.init_GUI()
		self.palette1 = QPalette()
		try:
			self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('th.jpeg')))
			self.setPalette(self.palette1)#set palette to draw the background
		except Exception as e:
			print('setting bg failed')



	def init_GUI(self):

		v_box = QVBoxLayout()
		self.sld.setMinimum(1)
		self.sld.setMaximum(150)
		# self.sld.setTickInterval(10)
		self.sld.setValue(25)
		# self.sld.setTickPosition(QSlider.TicksBelow)


		h_box = QHBoxLayout()
		h_box.addWidget(self.l)
		h_box.addWidget(self.sld)
		# h_box.addWidget(self.b)

		h2= QHBoxLayout()
		h2.addWidget(self.tm)
		h2.addStretch()
		h2.addStretch()
		h2.addWidget(QLabel('                 '))
		h2.addWidget(self.b)

		v_box.addLayout(h_box)
		v_box.addStretch()
		v_box.addStretch()
		v_box.addLayout(h2)

		self.ptm = Process(target=self.t_m, args=(self.q, ))
		self.th = threading.Thread(target=self.s_t, name='LoopThread')


		self.sld.valueChanged.connect(self.v_change)
		self.b.clicked.connect(self.timer_start)


		self.setLayout(v_box)
		self.setGeometry(500,150,200,208)
		self.setWindowTitle('tomato')
		self.setWindowFlags(Qt.WindowMinimizeButtonHint)
		self.setFixedSize(self.width(), self.height())

		try:
			self.setWindowIcon(QIcon('th.jpeg'))#  set icon
		except Exception as e:
			print('setting icon failed')


		self.show()

	def v_change(self):
		self.l.setText(str(self.sld.value()))
		self.tm.setText(str(self.sld.value())+':00')

	def playsound(self):
		print('loud noise !!!!!!!')
		os.system("google-chrome "+str(random.randint(1,4))+".mp3")

	def t_m(self,q):
		print('start timer')
		a = int(self.l.text())
		print(a)
		a = a*60    #seconds
		start_t = time.time()
		t_left = a
		while t_left>0:
			time.sleep(1)
			t = time.time()
			t_left = a - (t - start_t)
			sec = int(t_left%60)
			minu = int(t_left/60)
			q.put(str(minu)+':'+str(sec))
		self.playsound()
		#play sound
	def s_t(self):
		while True:
			a = self.q.get(True)
			print(a)
			self.tm.setText(a)
			time.sleep(0.1)

	def timer_start(self):
		# self.th.join()
		try:
			self.ptm.start()
			self.th.start()
		except Exception as e:
			print()

		print('start timer')
		if self.b.text()=='NEWtomato':
			self.ptm.terminate()
			print('terminated')
			self.ptm = Process(target=self.t_m, args=(self.q, ))
			self.ptm.start()

		self.b.setText('NEWtomato')

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 'You sure to quit?',QMessageBox.Yes | QMessageBox.No |  QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			self.ptm.terminate()
			print('terminated!!!')
			os.close()      #Don know how to close the whole thing ,  so create an error.................................
		else:
			event.ignore()

app = QApplication(sys.argv)
a_window = Patatoaaa()
sys.exit(app.exec_())