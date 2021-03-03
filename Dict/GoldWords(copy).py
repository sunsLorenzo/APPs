#coding: utf-8
import sys,os,time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  
import time,threading
from multiprocessing import Process, Queue
import random
import mysql.connector
num=30
##########################################################################################################################################################
class New_B(QDialog):
	"""docstring for ClassName"""
	def __init__(self):
		super().__init__()
		self.l1=QLabel('input__ENG_file:')
		self.ed1=QLineEdit()
		self.l2=QLabel('input__CHN_file:')
		self.ed2=QLineEdit()
		self.cmb = QComboBox()
		self.cmb.addItem('shuffle')
		self.cmb.addItem('NO_shuffle')

		self.b = QPushButton('LoadBook')
		self.tablename=QLineEdit('a')
		self.initGUI()

	def initGUI(self):
		v_box = QVBoxLayout()
		v_box.addWidget(self.l1)
		v_box.addWidget(self.ed1)
		v_box.addWidget(self.l2)
		v_box.addWidget(self.ed2)
		
		
		v_box.addWidget(QLabel('BookNameYou_wanna_save:'))
		v_box.addWidget(self.tablename)
		v_box.addWidget(self.cmb)
		v_box.addWidget(self.b)
		self.b.clicked.connect(self.btn_clkd)
		self.setLayout(v_box)
		self.setGeometry(600,0,250,280)
		self.show()
	def btn_clkd(self):
		print('New_Bbtn clicked')
		if ''!=self.ed1.text() and ''!=self.ed2.text() and 'please input the file names'!=self.ed2.text() and 'please input the file names'!=self.ed1.text() :
			try:
				conn = mysql.connector.connect(user='root', password='sunsong,.', database='worddb')
				cursor = conn.cursor()
				# 创建user表:
				cursor.execute('drop table '+self.tablename.text())
				cursor.execute('create table '+self.tablename.text()+'(ID int(20) not null AUTO_INCREMENT, ENG varchar(30) not null,CHN varchar(50) not null, star int not null,primary key(ID));')
				# 插入一行记录，注意MySQL的占位符是%s:
				L,Le,Lc=[],[],[]
				with open(self.ed1.text(), 'r') as e:
					for line in e.readlines():
						line = line.strip('\n')
						Le.append(line)
					print(Le)

				with open(self.ed2.text(), 'r') as c:
					for line in c.readlines():
						line = line.strip('\n')
						Lc.append(line)
					print(Lc)
				###格式化:
				for i in range(len(Le)):
					L.append([Le[i],Lc[i]])
				print(L)
				####打乱:
				if self.cmb.currentText()=='shuffle':
					random.shuffle(L)

				#存入数据库:
				for x in L:
					cursor.execute('insert into '+self.tablename.text()+' (ENG, CHN, star) values (%s, %s, %s)', (x[0],x[1],'1'))
					# print('rowcount =', cursor.rowcount)
				print('saved in DB')
				# 提交事务:
				conn.commit()
				cursor.close()
				conn.close()
				#进行文件的读取规整,录入数据库
			except Exception as e:
				print(e)
		else:
			self.ed1.setText('please input the file names')
			self.ed2.setText('please input the file names')


###################################################################################################################################################################
class Table_dia(QDialog):
	def __init__(self,l):
		super().__init__()
		v_box=QVBoxLayout()
		IDlb,star_ld = ['']*len(l), ['']*len(l)
		self.btn = QPushButton('Confirm')
		self.tablew = QTableWidget()
		self.tablew.setRowCount(len(l))
		self.tablew.setColumnCount(4)
		for i in range(4):
			self.tablew.setColumnWidth(i,200)
		for i in range(len(l)):
			for j in range(4):
				self.tablew.setItem(i,j,QTableWidgetItem(str(l[i][j])))
		v_box.addWidget(self.tablew)
		v_box.addWidget(self.btn)		
		self.btn.clicked.connect(self.btn_clkd)
		self.setLayout(v_box)
		self.setGeometry(500,0,1365,720)
		self.show()
		print(l)

	def btn_clkd(self):
		# a=Table_dia()
		# a.exec_()  #exec_()  关闭这个窗口后下一行才会执行
		print('confirm')

		#从table中读取ID值和star 值  修改数据库
		L=[]
		for row in range(self.tablew.rowCount()):
			tw1 = self.tablew.item(row,0)
			tw2 = self.tablew.item(row,1)
			tw3 = self.tablew.item(row,2)
			tw4 = self.tablew.item(row,3)
			# print( tw1.text()+tw2.text()+tw3.text()+tw4.text())
			L.append( (tw1.text(),tw2.text(),tw3.text(),tw4.text()) )
		print(L)
		print('')
		

		try:
			for i in L:
				int(i[3])

			conn = mysql.connector.connect(user='root', password='sunsong,.', database='worddb')
			cursor = conn.cursor()
			for item in L:
				#
				cursor.execute('update a set star = %s where ID = %s ',(item[3], item[0]))
			conn.commit()
			cursor.close()
			conn.close()
		except Exception as e:
			self.btn.setText('please input digit in star (4)')
			print('update start false!!!')
			a=Mistake_dia('please input digit in star (4)','update star false!!!')
			a.exec_()
		self.close()


			# IDlb[i]=QLabel()
			# Elb[i]=QLabel()
			# CHNlb[i]=QLabel()
			# Starle[i]=QLineEdit()

##########################################################################################################################################################

class Words_dia(QDialog):
	def __init__(self,l,i):
		super().__init__()
		self.l = l
		self.i=i+1
		self.eng = QLabel( l[i][1]+"    "+str(self.i)+'of'+str(len(self.l)))
		cn = l[i][2]
		cn1 = l[random.randint(0,len(l)-1)][2]
		cn2 = l[random.randint(0,len(l)-1)][2]
		cn3 = l[random.randint(0,len(l)-1)][2]
		chnlist =[cn,cn1,cn2,cn3]
		random.shuffle(chnlist)
		print(chnlist)
		self.eng.setFont(QFont("Timers",12,QFont.Bold))
		self.chn1 = QPushButton(str(chnlist[0]))
		self.chn2 = QPushButton(str(chnlist[1]))
		self.chn3 = QPushButton(str(chnlist[2]))
		self.chn4 = QPushButton(str(chnlist[3]))

		v_box = QVBoxLayout()
		v_box.addWidget(self.eng)
		v_box.addWidget(self.chn1)
		v_box.addWidget(self.chn2)
		v_box.addWidget(self.chn3)
		v_box.addWidget(self.chn4)
		self.setLayout(v_box)
		self.chn1.clicked.connect(self.btn_clkd)
		self.chn2.clicked.connect(self.btn_clkd)
		self.chn3.clicked.connect(self.btn_clkd)
		self.chn4.clicked.connect(self.btn_clkd)
		self.setGeometry(600,0,250,280)
		self.palette1 = QPalette()
		try:
			self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('2.png')))   
			self.setPalette(self.palette1)#set palette to draw the background
		except Exception as e:
			print('setting bg failed')	
		self.show()
	def btn_clkd(self):
		print(self.i)
		print(self.l)
		if self.sender().text()==self.l[self.i-1][2]:					#正确  判断是不是最后一个单词, 如果不是-->下一个,如果是最后一个,则弹出result窗口
			# self.chn1.setText(self.l[self.i-1][2])
			# self.chn2.setText(self.l[self.i-1][2])
			# self.chn3.setText(self.l[self.i-1][2])
			# self.chn4.setText(self.l[self.i-1][2])
			time.sleep(1)
			self.close()
			if self.i>=len(self.l):
				aa=Result_dia()
				aa.exec_()
			else:
				a=Words_dia(self.l,self.i)
				a.exec_()

		else:					#错误
			###
			self.l.append(self.l[self.i-1])   #将错误的单词 append进 list 里面  star += 1  并更新数据库
			time.sleep(1)
			self.close()
			#更新数据库的star 值#############

			aaa=Mistake_dia(self.l[self.i-1][1],self.l[self.i-1][2])
			aaa.exec_()

			a=Words_dia(self.l,self.i)
			a.exec_()
		
		



class Mistake_dia(QDialog):
	def __init__(self,eng,chn):
		super().__init__()
		self.eng=QLabel(eng)
		self.chn=QLabel(chn)
		self.b=QPushButton('NEXT')
		v_box=QVBoxLayout()
		v_box.addWidget(self.eng)
		v_box.addWidget(self.chn)
		v_box.addWidget(self.b)
		
		self.eng.setFont(QFont("Timers",12,QFont.Bold))
		self.chn.setFont(QFont("Timers",12,QFont.Bold))

		self.b.clicked.connect(self.btn_clkd)
		self.setLayout(v_box)
		self.setGeometry(600,0,250,280)
		self.show()

	def btn_clkd(self):
		self.close()


##########################################################################################################################################################
class Result_dia(QDialog):
	def __init__(self):
		super().__init__()

		self.l1=QLabel('!!!!FINISH!!!!')
		self.l1.setFont(QFont("Timers",15,QFont.Bold))
		v_box=QVBoxLayout()
		v_box.addWidget(self.l1)
		self.setGeometry(600,0,250,280)
		self.setLayout(v_box)
		self.show()


##########################################################################################################################################################
class Main_w(QWidget):

	def __init__(self):
		super().__init__()
		self.combo = QComboBox()

		self.l1 = QLabel('list:')
		self.comb1 = QComboBox()
		self.l2 = QLabel('star:')
		self.comb2 = QComboBox()

		self.b1 = QPushButton('NewBook')
		self.b2 = QPushButton('view the list')
		self.b3 = QPushButton('  START  ')

		self.initGUI()

	def initGUI(self):
		#查数据库,算出有多少个list
		conn = mysql.connector.connect(user='root', password='sunsong,.', database='worddb')
		# # 运行查询:
		cursor = conn.cursor()
		# cursor.execute('select * from user where id = %s', ('1',))
		cursor.execute('select * from a')
		values = cursor.fetchall()
		print(values)
		# 关闭Cursor和Connection:
		cursor.close()
		conn.close()

		#for 循环 comb1.addItem :
		for i in range(int(len(values)/num)):
			self.comb1.addItem(str(i))

		for i in range(10):
			self.comb2.addItem(str(i))

		#设置布局
		h_box = QHBoxLayout()
		v_box = QVBoxLayout()

		h_box.addWidget(self.l1)
		h_box.addWidget(self.comb1)
		h_box.addWidget(self.l2)
		h_box.addWidget(self.comb2)
		v_box.addLayout(h_box)

		v_box.addWidget(self.b1)
		v_box.addWidget(self.b2)
		v_box.addWidget(self.b3)
		self.setLayout(v_box)

		#
		self.setGeometry(600,0,155,144)
		self.setWindowTitle('GOLDENWORDS.CHOPCHOP')
		self.setWindowIcon(QIcon('3.png'))
		self.show()
		#Actionlistenner
		self.b1.clicked.connect(self.btn_clkd)
		self.b2.clicked.connect(self.btn_clkd)
		self.b3.clicked.connect(self.btn_clkd)
		self.palette1 = QPalette()
		# try:
		# 	self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('3.png')))   
		# 	self.setPalette(self.palette1)#set palette to draw the background
		# except Exception as e:
		# 	print('setting bg failed')		
	def btn_clkd(self):
		if self.sender().text()=='NewBook':
			pass
			print('list',self.comb1.currentText())
			n=New_B()
			n.show()
			n.exec_()
			self.close()
			self.__init__()

		if self.sender().text()=='view the list':
			conn = mysql.connector.connect(user='root', password='sunsong,.', database='worddb')
			cursor = conn.cursor()
			cursor.execute('select * from a where ID between %s and %s and star >= %s ',(str( num*int(self.comb1.currentText())+1), str( num*(int(self.comb1.currentText())+1) ), self.comb2.currentText() ))
			l = cursor.fetchall()
			cursor.close()
			conn.close()

			print('list:   view')
			v=Table_dia(l)
			print("length of the l is :",len(l))
			v.show()
			v.exec_()
		if self.sender().text()=='  START  ':
			conn = mysql.connector.connect(user='root', password='sunsong,.', database='worddb')
			cursor = conn.cursor()
			cursor.execute('select * from a where ID between %s and %s and star >= %s ',(str( num*int(self.comb1.currentText())+1), str( num*(int(self.comb1.currentText())+1) ), self.comb2.currentText() ))
			print('start-----------------------start-----------------------start-----------------------start-----------------------')

			l = cursor.fetchall()
			print(l)
			cursor.close()
			conn.close()
			if len(l)>=1:
				w = Words_dia(l,0)
				w.exec_()
































app = QApplication(sys.argv)
mainwindowofGoldenWords = Main_w()
# asas=Result_dia()
sys.exit(app.exec_())


#######												mysql connector
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# ########## prepare ##########

# # install mysql-connector-python:
# # pip3 install mysql-connector-python --allow-external mysql-connector-python

# import mysql.connector

# # change root password to yours:
# conn = mysql.connector.connect(user='root', password='password', database='test')

# cursor = conn.cursor()
# # 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# # 提交事务:
# conn.commit()
# cursor.close()

# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()





 # create table book1
 #    (
 #    ID int(20) not null AUTO_INCREMENT,
 #    ENG varchar(30) not null,
 #    CHN varchar(50) not null,
 #    star int not null,
 #    primary key(ID)
 #    )
 #    ;


# mysql> set character_set_client=utf8;

# mysql> set character_set_connection=utf8;

# mysql> set character_set_database=utf8;

# mysql> set character_set_results=utf8;

# mysql> set character_set_server=utf8;

# mysql> set character_set_system=utf8;

# mysql> set collation_connection=utf8;

# mysql> set collation_database=utf8;

# mysql> set collation_server=utf8;

# alter database mydb character set utf8;
# create database mydb character set utf8;