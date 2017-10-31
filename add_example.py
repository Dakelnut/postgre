from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import *

import sys
app = QtWidgets.QApplication(sys.argv)
dialog_window = loadUi("test_add.ui")

grid = dialog_window.gridLayout

pos = [(0, 0),
            (1, 0)]

pos2 = [(0, 1),
            (1, 1)]
names1 = ['Cls', 'Bck',  'Close', '7']
names2 = [ 'Close', '7']
for i in range(len(pos)):
    button = QtWidgets.QLabel(names1[i])
    grid.addWidget(button, pos[i][0], pos[i][1])

for i in range(len(pos2)):
    button = QtWidgets.QComboBox()

    grid.addWidget(button, pos2[i][0], pos2[i][1])


dialog_window.exec_()
sys.exit()