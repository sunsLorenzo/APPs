#coding: utf-8
import os.path, time, sys, threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  
class Table(QWidget):
	def __init__(self):
		super().__init__()
		# self.setWindowFlags(Qt.SplashScreen)#取消标题栏和边框
		self.setWindowFlags(Qt.FramelessWindowHint )# no title
		self.width = 1366
		self.height = 768
		self.gridwidth = 200
		self.gridheight = 100

		# self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
		self.btn = QPushButton('Confirm')

		self.labelAlfa = QLabel()
		self.labelAlfa.setStyleSheet("background-color:rgb(156,245,186)")

	
		self.initGUI()



	def initGUI(self):

		self.day0 = QLabel()
		self.day0.setStyleSheet("background-color:rgb(156,245,186)")

		self.day0.setText("")
		self.day1 = QLabel()
		self.day1.setStyleSheet("background-color:rgb(156,245,186)")
		self.day1.setText("Sunday")
		self.day2 = QLabel()
		self.day2.setStyleSheet("background-color:rgb(156,245,186)")
		self.day2.setText("Monday")
		self.day3 = QLabel()
		self.day3.setStyleSheet("background-color:rgb(156,245,186)")
		self.day3.setText("Tuesday")
		self.day4 = QLabel()
		self.day4.setText("Wednsday")
		self.day4.setStyleSheet("background-color:rgb(156,245,186)")
		self.day5 = QLabel()
		self.day5.setStyleSheet("background-color:rgb(156,245,186)")
		self.day5.setText("Thursday")
		self.day6 = QLabel()
		self.day6.setStyleSheet("background-color:rgb(156,245,186)")
		self.day6.setText("Friday")
		self.day7 = QLabel()
		self.day7.setStyleSheet("background-color:rgb(156,245,186)")
		self.day7.setText("Saturday")
		h_box1 = QHBoxLayout()
		h_box1.addWidget(self.day0)
		h_box1.addWidget(self.day1)
		h_box1.addWidget(self.day2)
		h_box1.addWidget(self.day3)
		h_box1.addWidget(self.day4)
		h_box1.addWidget(self.day5)
		h_box1.addWidget(self.day6)
		h_box1.addWidget(self.day7)
		########
		self.time1 = QLabel()
		self.time1.setStyleSheet("background-color:rgb(167,0,28)")
		self.time1.setText(" 8 -10am")
		self.txt11 = QTextEdit()
		self.txt12 = QTextEdit()
		self.txt13 = QTextEdit()
		self.txt14 = QTextEdit()
		self.txt15 = QTextEdit()
		self.txt16 = QTextEdit()
		self.txt17 = QTextEdit()
		with open('txt11.txt', 'r') as c:
			self.txt11.setText(c.read())
		with open('txt12.txt', 'r') as c:
			self.txt12.setText(c.read())
		with open('txt13.txt', 'r') as c:
			self.txt13.setText(c.read())
		with open('txt14.txt', 'r') as c:
			self.txt14.setText(c.read())
		with open('txt15.txt', 'r') as c:
			self.txt15.setText(c.read())
		with open('txt16.txt', 'r') as c:
			self.txt16.setText(c.read())
		with open('txt17.txt', 'r') as c:
			self.txt17.setText(c.read())

		h_box11 = QHBoxLayout()
		# txt11.setStyleSheet("background-color:rgb(156,245,186)")
		# txt12.setStyleSheet("background-color:rgb(156,245,186)")
		# txt13.setStyleSheet("background-color:rgb(156,245,186)")
		# txt14.setStyleSheet("background-color:rgb(156,245,186)")
		# txt15.setStyleSheet("background-color:rgb(156,245,186)")
		# txt16.setStyleSheet("background-color:rgb(156,245,186)")
		# txt17.setStyleSheet("background-color:rgb(156,245,186)")
		
		h_box11.addWidget(self.time1)
		h_box11.addWidget(self.txt11)
		h_box11.addWidget(self.txt12)
		h_box11.addWidget(self.txt13)
		h_box11.addWidget(self.txt14)
		h_box11.addWidget(self.txt15)
		h_box11.addWidget(self.txt16)
		h_box11.addWidget(self.txt17)
		



		self.time2 = QLabel()
		self.time2.setStyleSheet("background-color:rgb(54,89,177)")
		self.time2.setText("10-12am")
		self.txt21 = QTextEdit()
		self.txt22 = QTextEdit()
		self.txt23 = QTextEdit()
		self.txt24 = QTextEdit()
		self.txt25 = QTextEdit()
		self.txt26 = QTextEdit()
		self.txt27 = QTextEdit()
		with open('txt21.txt', 'r') as c:
			self.txt21.setText(c.read())
		with open('txt22.txt', 'r') as c:
			self.txt22.setText(c.read())
		with open('txt23.txt', 'r') as c:
			self.txt23.setText(c.read())
		with open('txt24.txt', 'r') as c:
			self.txt24.setText(c.read())
		with open('txt25.txt', 'r') as c:
			self.txt25.setText(c.read())
		with open('txt26.txt', 'r') as c:
			self.txt26.setText(c.read())
		with open('txt27.txt', 'r') as c:
			self.txt27.setText(c.read())
		# txt21.setStyleSheet("background-color:rgb(156,245,186)")
		# txt22.setStyleSheet("background-color:rgb(156,245,186)")
		# txt23.setStyleSheet("background-color:rgb(156,245,186)")
		# txt24.setStyleSheet("background-color:rgb(156,245,186)")
		# txt25.setStyleSheet("background-color:rgb(156,245,186)")
		# txt26.setStyleSheet("background-color:rgb(156,245,186)")
		# txt27.setStyleSheet("background-color:rgb(156,245,186)")
		h_box21 = QHBoxLayout()
		h_box21.addWidget(self.time2)
		h_box21.addWidget(self.txt21)
		h_box21.addWidget(self.txt22)
		h_box21.addWidget(self.txt23)
		h_box21.addWidget(self.txt24)
		h_box21.addWidget(self.txt25)
		h_box21.addWidget(self.txt26)
		h_box21.addWidget(self.txt27)


		self.time3 = QLabel()
		self.time3.setStyleSheet("background-color:rgb(0,196,0)")
		self.time3.setText("14-16pm")
		self.txt31 = QTextEdit()
		self.txt32 = QTextEdit()
		self.txt33 = QTextEdit()
		self.txt34 = QTextEdit()
		self.txt35 = QTextEdit()
		self.txt36 = QTextEdit()
		self.txt37 = QTextEdit()

		with open('txt31.txt', 'r') as c:
			self.txt31.setText(c.read())
		with open('txt32.txt', 'r') as c:
			self.txt32.setText(c.read())
		with open('txt33.txt', 'r') as c:
			self.txt33.setText(c.read())
		with open('txt34.txt', 'r') as c:
			self.txt34.setText(c.read())
		with open('txt35.txt', 'r') as c:
			self.txt35.setText(c.read())
		with open('txt36.txt', 'r') as c:
			self.txt36.setText(c.read())
		with open('txt37.txt', 'r') as c:
			self.txt37.setText(c.read())
		# txt31.setStyleSheet("background-color:rgb(156,245,186)")
		# txt32.setStyleSheet("background-color:rgb(156,245,186)")
		# txt33.setStyleSheet("background-color:rgb(156,245,186)")
		# txt34.setStyleSheet("background-color:rgb(156,245,186)")
		# txt35.setStyleSheet("background-color:rgb(156,245,186)")
		# txt36.setStyleSheet("background-color:rgb(156,245,186)")
		# txt37.setStyleSheet("background-color:rgb(156,245,186)")
		h_box31 = QHBoxLayout()
		h_box31.addWidget(self.time3)
		h_box31.addWidget(self.txt31)
		h_box31.addWidget(self.txt32)
		h_box31.addWidget(self.txt33)
		h_box31.addWidget(self.txt34)
		h_box31.addWidget(self.txt35)
		h_box31.addWidget(self.txt36)
		h_box31.addWidget(self.txt37)

		self.time4 = QLabel()
		self.time4.setStyleSheet("background-color:rgb(254,183,0)")
		self.time4.setText("16-18am")
		self.txt41 = QTextEdit()
		self.txt42 = QTextEdit()
		self.txt43 = QTextEdit()
		self.txt44 = QTextEdit()
		self.txt45 = QTextEdit()
		self.txt46 = QTextEdit()
		self.txt47 = QTextEdit()

		with open('txt41.txt', 'r') as c:
			self.txt41.setText(c.read())
		with open('txt42.txt', 'r') as c:
			self.txt42.setText(c.read())
		with open('txt43.txt', 'r') as c:
			self.txt43.setText(c.read())
		with open('txt44.txt', 'r') as c:
			self.txt44.setText(c.read())
		with open('txt45.txt', 'r') as c:
			self.txt45.setText(c.read())
		with open('txt46.txt', 'r') as c:
			self.txt46.setText(c.read())
		with open('txt47.txt', 'r') as c:
			self.txt47.setText(c.read())
		# txt41.setStyleSheet("background-color:rgb(156,245,186)")
		# txt42.setStyleSheet("background-color:rgb(156,245,186)")
		# txt43.setStyleSheet("background-color:rgb(156,245,186)")
		# txt44.setStyleSheet("background-color:rgb(156,245,186)")
		# txt45.setStyleSheet("background-color:rgb(156,245,186)")
		# txt46.setStyleSheet("background-color:rgb(156,245,186)")
		# txt47.setStyleSheet("background-color:rgb(156,245,186)")
		h_box41 = QHBoxLayout()
		h_box41.addWidget(self.time4)
		h_box41.addWidget(self.txt41)
		h_box41.addWidget(self.txt42)
		h_box41.addWidget(self.txt43)
		h_box41.addWidget(self.txt44)
		h_box41.addWidget(self.txt45)
		h_box41.addWidget(self.txt46)
		h_box41.addWidget(self.txt47)


		self.time5 = QLabel()
		self.time5.setStyleSheet("background-color:rgb(1,10,54)")
		self.time5.setText("Evening_ ")
		self.txt51 = QTextEdit()
		self.txt52 = QTextEdit()
		self.txt53 = QTextEdit()
		self.txt54 = QTextEdit()
		self.txt55 = QTextEdit()
		self.txt56 = QTextEdit()
		self.txt57 = QTextEdit()

		with open('txt51.txt', 'r') as c:
			self.txt51.setText(c.read())
		with open('txt52.txt', 'r') as c:
			self.txt52.setText(c.read())
		with open('txt53.txt', 'r') as c:
			self.txt53.setText(c.read())
		with open('txt54.txt', 'r') as c:
			self.txt54.setText(c.read())
		with open('txt55.txt', 'r') as c:
			self.txt55.setText(c.read())
		with open('txt56.txt', 'r') as c:
			self.txt56.setText(c.read())
		with open('txt57.txt', 'r') as c:
			self.txt57.setText(c.read())
		# txt51.setStyleSheet("background-color:rgb(156,245,186)")
		# txt52.setStyleSheet("background-color:rgb(156,245,186)")
		# txt53.setStyleSheet("background-color:rgb(156,245,186)")
		# txt54.setStyleSheet("background-color:rgb(156,245,186)")
		# txt55.setStyleSheet("background-color:rgb(156,245,186)")
		# txt56.setStyleSheet("background-color:rgb(156,245,186)")
		# txt57.setStyleSheet("background-color:rgb(156,245,186)")
		h_box51 = QHBoxLayout()
		h_box51.addWidget(self.time5)
		h_box51.addWidget(self.txt51)
		h_box51.addWidget(self.txt52)
		h_box51.addWidget(self.txt53)
		h_box51.addWidget(self.txt54)
		h_box51.addWidget(self.txt55)
		h_box51.addWidget(self.txt56)
		h_box51.addWidget(self.txt57)





		v_box = QVBoxLayout()
		# v_box.addWidget(self.label)
		# v_box.addWidget(QLabel().setText("sad"))
		v_box.addWidget(self.labelAlfa)
		v_box.addLayout(h_box1)
		v_box.addLayout(h_box11)
		v_box.addLayout(h_box21)
		v_box.addLayout(h_box31)
		v_box.addLayout(h_box41)
		v_box.addLayout(h_box51)
		# v_box.addWidget(self.tablew)
		self.setLayout(v_box)
		self.setGeometry(500,0,1365,720)



		try:
			self.setWindowIcon(QIcon('th.png'))#  set icon
		except Exception as e:
			print('setting icon failed')
		self.show()

	##################################实现移动窗体:############################################
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QApplication.postEvent(self, QEvent(174))
			event.accept()
			with open('setGeometry.txt', 'w') as h:
				h.write(str(self.frameGeometry()))

		if event.button() == Qt.RightButton:
			self.close()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 'You sure to quit?',QMessageBox.Yes | QMessageBox.No |  QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			self.ptm.terminate()
			print('terminated!!!')
			os.close()      #Don know how to close the whole thing ,  so create an error.................................
		else:
			event.ignore()

	def leaveEvent (self, event):
		print("out&saving")
		####save the text into file 
		with open('txt11.txt', 'w') as f:
			f.write(self.txt11.toPlainText())      #写文件
		with open('txt12.txt', 'w') as f:
			f.write(self.txt12.toPlainText())      #写文件
		with open('txt13.txt', 'w') as f:
			f.write(self.txt13.toPlainText())      #写文件
		with open('txt14.txt', 'w') as f:
			f.write(self.txt14.toPlainText())     
		with open('txt15.txt', 'w') as f:
			f.write(self.txt15.toPlainText())      
		with open('txt16.txt', 'w') as f:
			f.write(self.txt16.toPlainText())      
		with open('txt17.txt', 'w') as f:
			f.write(self.txt17.toPlainText())      

###
		with open('txt21.txt', 'w') as f:
			f.write(self.txt21.toPlainText())      #写文件
		with open('txt22.txt', 'w') as f:
			f.write(self.txt22.toPlainText())      #写文件
		with open('txt23.txt', 'w') as f:
			f.write(self.txt23.toPlainText())      #写文件
		with open('txt24.txt', 'w') as f:
			f.write(self.txt24.toPlainText())      #写文件
		with open('txt25.txt', 'w') as f:
			f.write(self.txt25.toPlainText())      #写文件
		with open('txt26.txt', 'w') as f:
			f.write(self.txt26.toPlainText())      #写文件
		with open('txt27.txt', 'w') as f:
			f.write(self.txt27.toPlainText())      #写文件


		with open('txt31.txt', 'w') as f:
			f.write(self.txt31.toPlainText())      #写文件
		with open('txt32.txt', 'w') as f:
			f.write(self.txt32.toPlainText())      #写文件
		with open('txt33.txt', 'w') as f:
			f.write(self.txt33.toPlainText())      #写文件
		with open('txt34.txt', 'w') as f:
			f.write(self.txt34.toPlainText())      #写文件
		with open('txt35.txt', 'w') as f:
			f.write(self.txt35.toPlainText())      #写文件
		with open('txt36.txt', 'w') as f:
			f.write(self.txt36.toPlainText())      #写文件
		with open('txt37.txt', 'w') as f:
			f.write(self.txt37.toPlainText())      #写文件

		with open('txt41.txt', 'w') as f:
			f.write(self.txt41.toPlainText())      #写文件
		with open('txt42.txt', 'w') as f:
			f.write(self.txt42.toPlainText())      #写文件
		with open('txt43.txt', 'w') as f:
			f.write(self.txt43.toPlainText())      #写文件
		with open('txt44.txt', 'w') as f:
			f.write(self.txt44.toPlainText())      #写文件
		with open('txt45.txt', 'w') as f:
			f.write(self.txt45.toPlainText())      #写文件
		with open('txt46.txt', 'w') as f:
			f.write(self.txt46.toPlainText())      #写文件
		with open('txt47.txt', 'w') as f:
			f.write(self.txt47.toPlainText())      #写文件

		with open('txt51.txt', 'w') as f:
			f.write(self.txt51.toPlainText())      #写文件
		with open('txt52.txt', 'w') as f:
			f.write(self.txt52.toPlainText())      #写文件
		with open('txt53.txt', 'w') as f:
			f.write(self.txt53.toPlainText())      #写文件
		with open('txt54.txt', 'w') as f:
			f.write(self.txt54.toPlainText())      #写文件
		with open('txt55.txt', 'w') as f:
			f.write(self.txt55.toPlainText())      #写文件
		with open('txt56.txt', 'w') as f:
			f.write(self.txt56.toPlainText())      #写文件
		with open('txt57.txt', 'w') as f:
			f.write(self.txt57.toPlainText())      #写文件
app = QApplication(sys.argv)
pad = Table()
sys.exit(app.exec_())