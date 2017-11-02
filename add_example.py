from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import *
#
# import sys
# app = QtWidgets.QApplication(sys.argv)
# dialog_window = loadUi("test_add.ui")
#
# grid = dialog_window.gridLayout
#
# pos = [(0, 0),
#             (1, 0)]
#
# pos2 = [(0, 1),
#             (1, 1)]
# names1 = ['Cls', 'Bck',  'Close', '7']
# names2 = [ 'Close', '7']
# for i in range(len(pos)):
#     button = QtWidgets.QLabel(names1[i])
#     grid.addWidget(button, pos[i][0], pos[i][1])
#
# for i in range(len(pos2)):
#     button = QtWidgets.QComboBox()
#
#     grid.addWidget(button, pos2[i][0], pos2[i][1])
#
#
# dialog_window.exec_()
# sys.exit()
# import sys
# flag =  True
# def conn():
#     global flag
#     if flag == True:
#         frame.hide()
#         flag = not flag
#     else:
#         frame.show()
#         flag = not flag
#
# app = QtWidgets.QApplication(sys.argv)
# window = loadUi("test_frame.ui")
# frame = window.frame
# butt = window.pushButton
# butt.clicked.connect(conn)
# window.show()
# sys.exit(app.exec_())

#
# import sys
#
#
# ####################################################################
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     w = MyWindow()
#     w.show()
#     sys.exit(app.exec_())
#
# ####################################################################
# class MyWindow(QtWidgets.QWidget):
#     def __init__(self, *args):
#         QtWidgets.QWidget.__init__(self, *args)
#
#         # create objects
#         list_data = [1,2,3,4]
#         lm = MyListModel(list_data, self)
#         de = MyDelegate(self)
#         lv = QtWidgets.QListView()
#         lv.setModel(lm)
#         lv.setItemDelegate(de)
#
#         # layout
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(lv)
#         self.setLayout(layout)
#
# ####################################################################
# class MyDelegate(QtWidgets.QItemDelegate):
#     def __init__(self, parent=None, *args):
#         QtWidgets.QItemDelegate.__init__(self, parent, *args)
#
#     def paint(self, painter, option, index):
#         painter.save()
#
#         # set background color
#         painter.setPen(QtWidgets.QPen(QtWidgets.Qt.NoPen))
#         if option.state & QtWidgets.QStyle.State_Selected:
#             painter.setBrush(QtWidgets.QBrush(QtWidgets.Qt.red))
#         else:
#             painter.setBrush(QtWidgets.QBrush(QtWidgets.Qt.white))
#         painter.drawRect(option.rect)
#
#         # set text color
#         painter.setPen(QtWidgets.QPen(QtWidgets.Qt.black))
#         value = index.data(QtWidgets.Qt.DisplayRole)
#         if value.isValid():
#             text = value.toString()
#             painter.drawText(option.rect, QtWidgets.Qt.AlignLeft, text)
#
#         painter.restore()
#
# ####################################################################
# class MyListModel(QtWidgets.QAbstractListModel):
#     def __init__(self, datain, parent=None, *args):
#         """ datain: a list where each item is a row
#         """
#         QtWidgets.QAbstractTableModel.__init__(self, parent, *args)
#         self.listdata = datain
#
#     def rowCount(self, parent=QtWidgets.QModelIndex()):
#         return len(self.listdata)
#
#     def data(self, index, role):
#         if index.isValid() and role == QtWidgets.Qt.DisplayRole:
#             return QtWidgets.QVariant(self.listdata[index.row()])
#         else:
#             return QtWidgets.QVariant()
#
# ####################################################################
# if __name__ == "__main__":
#     main()

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class HTMLDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__()
        self.doc = QTextDocument(self)

    def paint(self, painter, option, index):
        painter.save()

        options = QStyleOptionViewItem(option)

        self.initStyleOption(options, index)
        self.doc.setHtml(options.text)
        options.text = ""

        style = QApplication.style() if options.widget is None \
            else options.widget.style()
        style.drawControl(QStyle.CE_ItemViewItem, options, painter)

        ctx = QAbstractTextDocumentLayout.PaintContext()

        print(QStyle.State_Selected)

        if option.state & QStyle.State_Selected:
            ctx.palette.setColor(QPalette.Text, option.palette.color(
                QPalette.Active, QPalette.HighlightedText))
        else:
            ctx.palette.setColor(QPalette.Text, option.palette.color(
                QPalette.Active, QPalette.Text))

        textRect = style.subElementRect(
            QStyle.SE_ItemViewItemText, options)

        if index.column() != 0:
            textRect.adjust(5, 0, 0, 0)

        thefuckyourshitup_constant = 4
        margin = (option.rect.height() - options.fontMetrics.height()) // 2
        margin = margin - thefuckyourshitup_constant
        textRect.setTop(textRect.top() + margin)

        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        self.doc.documentLayout().draw(painter, ctx)

        painter.restore()

    def sizeHint(self, option, index):
        return QSize(self.doc.idealWidth(), self.doc.size().height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = ['1','2','3','4','5','6','7','8','9']
    main_list = QListView()
    main_list.setItemDelegate(HTMLDelegate())
    main_list.setModel(QStringListModel(data))
    main_list.show()
    sys.exit(app.exec_())

# from PyQt5 import QtWidgets,QtGui, QtCore
# import sys
#
# class Main( QtWidgets.QMainWindow):
#     def __init__(self, parent = None):
#         QtWidgets.QMainWindow.__init__(self,parent)
#         self.initUI()
#
#     def initUI(self):
#         mylist = QtWidgets.QListWidget(self)
#         mylist.setMinimumSize(QtCore.QSize(800, 800))
#         for i in range(5):
#             widgitItem = QtWidgets.QListWidgetItem()
#             widget = QtWidgets.QWidget()
#             widgetText =  QtWidgets.QLabel('test<span style="color:#ff0000;">test %s</span>' % (i + 1))
#             widgetLayout = QtWidgets.QHBoxLayout()
#             widgetLayout.addWidget(widgetText)
#             widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
#             widget.setLayout(widgetLayout)
#             mylist.addItem(widgitItem)
#             widgitItem.setSizeHint(widget.sizeHint())
#             mylist.setItemWidget(widgitItem, widget)
#
#
# def main():
#     app =QtWidgets.QApplication(sys.argv)
#     main = Main()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import sys
#
# my_array = [['00','01','02'],
#             ['10','11','12'],
#             ['20','21','22']]
#
# def main():
#     app = QApplication(sys.argv)
#     w = MyWindow()
#     w.show()
#     sys.exit(app.exec_())
#
# class MyWindow(QTableView):
#     def __init__(self, *args):
#         QTableView.__init__(self, *args)
#
#         tablemodel = MyTableModel(my_array, self)
#         self.setModel(tablemodel)
#
# class MyTableModel(QAbstractTableModel):
#     def __init__(self, datain, parent=None, *args):
#         QAbstractTableModel.__init__(self, parent, *args)
#         self.arraydata = datain
#
#     def rowCount(self, parent):
#         return len(self.arraydata)
#
#     def columnCount(self, parent):
#         return len(self.arraydata[0])
#
#     def data(self, index, role):
#         if not index.isValid():
#             return QVariant()
#         # vvvv this is the magic part
#         elif role == Qt.BackgroundRole:
#             if self.arraydata[index.row()][index.column()] == '20':
#                 return QBrush(Qt.yellow)
#             else:
#                 return QBrush(Qt.red)
#         # ^^^^ this is the magic part
#         elif role != Qt.DisplayRole:
#             return QVariant()
#         return QVariant(self.arraydata[index.row()][index.column()])
#     #
#     # def data(self, index, role):
#     #     print(index.row())
#     #     if index.isValid():
#     #         if role == Qt.ForegroundRole and self.item(index) == '555':
#     #             return QBrush(Qt.red)
#
# if __name__ == "__main__":
#     main()