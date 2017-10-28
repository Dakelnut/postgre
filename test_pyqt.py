
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

import sys

app = QApplication(sys.argv)
window = loadUi("db2.ui")



# dial.setNotchesVisible(True)



table = window.tableWidget

# lcdNumber = window.lcdNumber

# progressbar = window.progressBar
# def slider_changed():
#     lcdNumber.display(dial.value())
#     progressbar.setValue(dial.value())

# dial.valueChanged.connect(slider_changed)


# table.data.append([1,1,1,1,1])
data = {'Kitty': ['1', '2', '3', '3'],
        'Cat': ['4', '5', '6', '2'],
        'Meow': ['7', '8', '9', '5'],
        'Purr': ['4', '3', '4', '8'], }

table.setRowCount(4)
table.setColumnCount(4)
# table.insertRow(table.rowCount())
horHeaders = []
for n, key in enumerate(sorted(data.keys())):
    horHeaders.append(key)
    for m, item in enumerate(data[key]):
        newitem = QTableWidgetItem(item)
        table.setItem(m, n, newitem)
        table.item(m, n).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

table.setHorizontalHeaderLabels(horHeaders)
header = table.horizontalHeader()
# header.setStretchLastSection(True)
for i in range(header.count()):
    table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

# table.horizontalHeader().setMaximumWidth(float(table.width() / 4))
# # Adjust size of Table
# table.resizeColumnsToContents()
# table.resizeRowsToContents()

window.show()
sys.exit(app.exec_())

