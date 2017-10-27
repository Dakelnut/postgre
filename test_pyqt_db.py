import sys
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
# import sportsconnection


def initializeModel(model):
    model.setTable('cartel')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Baron name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Level of danger")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "Income")


def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def addrow():
    print( model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    delrow = i.row()

import psycopg2
def test():
    # Define our connection string
    conn_string = "host='localhost' dbname='ftest1' user='postgres' password='root'"

    # print the connection string we will use to connect
    print
    ("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")
    return conn


if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('POSTGRESQL')
    db.setDatabaseName('sports.db')
    # model = QtSql.QSqlTableModel()
    # model = test()
    delrow = -1
    # initializeModel(model)
    model = test()
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())
