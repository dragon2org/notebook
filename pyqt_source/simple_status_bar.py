# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(250, 150)
        self.setWindowTitle("状态栏实例程序")
        #设置状态栏
        self.statusBar().showMessage("就绪")


app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())