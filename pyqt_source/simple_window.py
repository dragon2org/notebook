# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app  = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(400,400)
w.setWindowTitle('hello Qt')
w.show()
sys.exit(app.exec_())
