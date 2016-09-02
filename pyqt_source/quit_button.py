#-*- coding:utf-8 -*-
"""用按钮关闭程序"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class QuitButton(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("关闭程序")

        quit_button = QtWidgets.QPushButton("关闭", self)
        quit_button.setGeometry(10, 10, 60, 35)
        quit_button.clicked.connect(QtWidgets.qApp.quit)

app = QtWidgets.QApplication(sys.argv)
quitbutton = QuitButton()
quitbutton.show()
sys.exit(app.exec_())
