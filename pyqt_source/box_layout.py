#-*- coding: utf-8 -*-
"""Box布局演示"""
import sys
from PyQt5 import QtWidgets

class BoxLayout(QtWidgets.QWidget):
    def __init__(self):
        super(BoxLayout, self).__init__()

    self.setWindowTitle("box定位演示程序")
    self.ok_button = QtWidgets.QPushButton("确定")
    self.