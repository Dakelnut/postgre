
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

import sys

app = QApplication(sys.argv)
window = loadUi("db2.ui")



# dial.setNotchesVisible(True)


class MyWindow(QTableView):
    def __init__(self, *args):
        QTableView.__init__(self, *args)

        tablemodel = MyTableModel(my_array, self)
        self.setModel(tablemodel)
table = window.tableWidget

# lcdNumber = window.lcdNumber

# progressbar = window.progressBar
# def slider_changed():
#     lcdNumber.display(dial.value())
#     progressbar.setValue(dial.value())

# dial.valueChanged.connect(slider_changed)


# table.data.append([1,1,1,1,1])
data = {'Kitty': ['132', '2', '3', '3'],
        'Cat': ['4', '555', '6', '2'],
        'Meow': ['7', '858', '9', '5'],
        'Purr': ['4', '3', '543', '8'], }

table.setRowCount(5)
table.setColumnCount(5)
# table.insertRow(table.rowCount())
horHeaders = []
for n, key in enumerate(sorted(data.keys())):
    horHeaders.append(key)
    for m, item in enumerate(data[key]):
        newitem = QTableWidgetItem(item)
        table.setItem(m, n, newitem)
        table.item(m, n).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

for i in range(4):
    table.setCellWidget(i, 4, QComboBox())

table.setHorizontalHeaderLabels(horHeaders)
header = table.horizontalHeader()
# header.setStretchLastSection(True)
for i in range(header.count()):
    table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

# table.horizontalHeader().setMaximumWidth(float(table.width() / 4))
# # Adjust size of Table
# table.resizeColumnsToContents()
# table.resizeRowsToContents()

# def my_partion(string,striper ):
#     f = list(string.partition(striper))
#     el = f[2]
#     while striper in el:
#         f.pop(len(f)-1)
#         buff = list(el.partition(striper))
#         f.append(buff)
#         el = buff[2]
#     return  f
# print(my_partion("55870955785435",'5'))


el = '555'
for i in range(table.rowCount()):
    for j in range(table.columnCount()):
        try:
            print(i,j)
            item = table.item(i,j)

            if item.text().find(el) != -1:
                newitem = QTableWidgetItem(item.text().replace(el,'<span style="color:#ff0000;">{0}</span>'.format(el)).setHmtl())
                # print("AAAA", split_items)
                table.setItem(i, j, newitem)
                # table.item(i,j).setBackground(QColor(125,125,125))
        except Exception as e:
            print(e)
            continue




window.show()
sys.exit(app.exec_())

