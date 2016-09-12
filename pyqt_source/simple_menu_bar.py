# -*- coding: utf-8 -*-
"""菜单栏"""
import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(250, 150)
        self.setWindowTitle("菜单栏示例")

        exit_menu = QtWidgets.QAction(QtGui.QIcon(r"sample_icon.ico"), "退出", self)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu("摸摸大")
        file.addAction(exit_menu)

app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())