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

#         self.setWindowFlags(Qt.SplashScreen)#取消标题栏和边框
#         self.setWindowFlags(Qt.CustomizeWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
        self.txt = QTextEdit()
        self.palette1 = QPalette()
        self.padding = 0
        # try:
        #     self.palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('green.png')))
        #     self.setPalette(self.palette1)#set palette to draw the background
        #     # self.txt.setPalette(self.palette1)
        # except Exception as e:
        #     print('setting bg failed')

        self.setWindowFlags(Qt.FramelessWindowHint )   #################无标题栏
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.label = QLabel()
        self.label.setFont(QFont("Timers",12,QFont.Bold))
        self.txt.setFont(QFont("Timers",10))
        # self.txt.setStyleSheet("color: rgb(255,255,255) ")

        # self.txt.setStyleSheet("background-image:url(bgbg.png)")
        self.label.setStyleSheet("background-color:rgb(249, 252, 255)")
        self.setStyleSheet("background-color:rgb(249, 252, 255)")
        # with open('setColor.txt', 'r') as c:

        #     self.label.setStyleSheet("background-color:rgb"+c.read())

        self.thd = threading.Thread(target=self.show_time, name='LoopThread')
        self.thd.start()
        self.initGUI()



    def initGUI(self):
        v_box = QVBoxLayout()

        v_box.addWidget(self.label)

        v_box.addWidget(self.txt)


        self.setLayout(v_box)
        # self.setStyleSheet("background-color:rgb(156,245,186)")
        # self.setStyleSheet("background-image:url(bgbg.png)")
        self.setGeometry(1679, 0, 300, 450)
        # with open('setGeometry.txt', 'r') as h:
        #     a = h.readline()[19:-1]
        #     a = list(a.split(','))
        #     print(a)
        #     self.setGeometry(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
        # self.setWindowTitle('Xpad')

        # self.setWindowFlags(Qt.WindowMinimizeButtonHint) #设置为不能最大化
        # self.setFixedSize(self.width(), self.height())  #  size fixed

        # self.txt.setStyleSheet('background-color:rgb(235,235,235));'  'color: rgb(255,255,255) ;')
        # with open('setColor.txt', 'r') as c:

        #     self.txt.setStyleSheet("background-color:rgb"+c.read())


        with open('XpadText.txt', 'r') as f:
            self.txt.setText(f.read())                ####读文件


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
            time.sleep(1)

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

    def mouseDoubleClickEvent(self,event):
        if self.flag == 1:
                self.setGeometry(1679, 0, 300, 450)
                self.flag = 2
        else:
            self.flag = 1
            self.setGeometry(1679, 0, 666, 768)
        self.txt.setFont(QFont("Timers",12,))
        self.txt.setText(self.txt.toPlainText())


##############################################################################
    def enterEvent(self, event):
        # self.txt.setStyleSheet("color: rgb(255,255,255) ")


        # self.label.setStyleSheet("background-color:rgb(235,235,235)")
        # self.setStyleSheet("background-color:rgb(235,235,235)")
        print("enter")

    def leaveEvent (self, event):
        # self.setWindowFlags(Qt.SplashScreen)#取消标题栏
        # self.setAttribute(Qt.WA_TranslucentBackground, True)#边框透明
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)

        # self.txt.setStyleSheet("color: rgb(0,0,0) ")
        # self.label.setStyleSheet("background-color:rgb(235,235,235)")
        # self.setStyleSheet("background-color:rgb(235,235,235)")

        print("out&saving")
        ####save the text into file
        with open('XpadText.txt', 'w') as f:
            f.write(self.txt.toPlainText())      #写文件


#         with open('test.txt', 'w') as f:
#        f.write('Hello, worlddadasdsads!')
# #覆盖



# 3. 鼠标移进和移出控件
#     鼠标移进和移出控件时，下列方法将被调用：

#     enterEvent (self, event) -鼠标进入控件;
#     leaveEvent (self, event) - 鼠标离开控件;

app = QApplication(sys.argv)
# version = 0.1
# if os.path.exists(os.environ['HOME'] +'/Documents/Xpad'+ '/.Xpad.pkl'):
#     fl = open(os.environ['HOME'] +'/Documents/Xpad'+ '/.Xpad.pkl', 'rb')

# else:
#     fl = open(os.environ['HOME'] +'/Documents/Xpad'+ '/.Xpad.png', 'wb')
#     fl.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1f\x00\x00\x00\x1e\x08\x02\x00\x00\x00[\x90R\xcb\x00\x00\x00\tpHYs\x00\x00\x0e\xc4\x00\x00\x0e\xc4\x01\x95+\x0e\x1b\x00\x00\x01\xa0IDATH\x89\xb5\x96?K\xc3@\x18\xc6\x9f;\x13\x13i\xa9\x7f:\xa8X\x17\x15D\x14\x17\xa9\xd4\x0f \n.\xeaP\xa8\xdf@\xdc\x9ct\xe8*:\xfa\x11\x9c\xd4I\'\xa9\x83kA\xb0\x8b\xe0\xe0Z\x10\x1cjk\x8b\xc5\x84F\xcf\xc1j\xd3\xf4.\xd7\\\xc93\xe5\xee\xbd\xfb\x1d<y\xdeK\x08\xc6S \x08$\xe1\xf2\x8e\x02\r\x0f\r\x80\x86\x87\x06\xa0\xb9\x07\xc9Y\xe303\xac\xebr\x9aH\x8d\x06;\xbax/<[\x1c\xfa\xfe\x16\xd9\\z\rJ\xf4\xc8\xb6\xcc\x9d\x93\xe6s\x9b3\x14V\x8fh\x0f$\x98\xef\xc1O\nS\x9a|Ip14\x03!\xa1\x9f\xe7J\xe5\xda\x97\xa8:3i\xac\xad\x0cq\n\x7fY\x93\xd0\x97\x17\xa2\x96\xcdD\xd5\xc1h\x9f\xffv\t\xbd\\u\xea\xd6\xb7\xcf\x82\xc4h/\xf4\x9aS\xfd\x10:c\xe8\x92v\x93\xd0\x93\xf3Q\xc7\x11:c\x1a\x92\xc8I\xdf\xea[\xa9\xd2\x10U\xe7\xa6\x06\xd2\xabqu\xfa^\xda\xd7W\x99T\x12\x99Y\x8f\x8f\xc4\xbaj\x14\x95DFL\x8a\xfe1\x12Kq[\xbdl?\x00\xc5\xae\xe8\xd3\t\x93;O"\x8b\xd09\x8e\xdf\xdc\xdd\xef\x9e\x16\xff\x87\xaa\xf7\x0cs:\xe7\xaer\xf9\x8d\x83G\xf7\x0c%\n\xdf\x08\x9e\xaer\xf9\xed\xec\x13\x88\xe7J\x07\xd0\xf3\x01\\4\xda\x9cQ=A\x84n\xd1Y\x08h\x00\x9a2W\x82&\x80\'3\xb6\xb0\xe79\xba\xbe\x95\xa0\xe1\xc9\xfb\xf1\xa5S\xff\x84\xd1E\x1b\xbe\xd4\n\xd9\xb3\x8a?\x1a\x00\xc1D\xcaUa`~\xb7\xb9k\x1f\x11y\xed\xa6k\xbf_\xc1\x96(UO\x0f\xe7?\x92S\x16^\xe8\x81\xd0\x00~\x00\xfd%rk\xc5\xfax\xdf\x00\x00\x00\x00IEND\xaeB`\x82'
#         # 图标二进制数据
#         )
#     fl.close()

#         # 启动器图标所需内容
# content = '''[Desktop Entry]
# Encoding=UTF-8
# Name=Xpad
# Comment=xpad
# Exec=python3 {}
# Icon={}
# Categories=Application;
# Version={}
# Type=Application
# Terminal=false\n'''.format(os.getcwd() + '/Xpad.py', os.environ['HOME'] + '/.Xpad.png', version)
# path = os.environ['HOME'] + '/.local/share/applications/' + 'Xpad.desktop'
# fl = open(path, 'w')
# fl.write(content)
# fl.close()

pad = Xpad()
sys.exit(app.exec_())