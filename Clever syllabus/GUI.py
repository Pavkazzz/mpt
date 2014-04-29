#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
button = QtGui.QPushButton()

widget.show()

sys.exit(app.exec_())
