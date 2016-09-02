#-*- coding:utf-8 -*-
""""重定义关闭事件"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MessageBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("关闭消息时间")

    def closeEvent(self, QCloseEvent):
        replay = QtWidgets.QMessageBox.question(self, "确认退出", "取消", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if replay == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QtWidgets.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())