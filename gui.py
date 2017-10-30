from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets

import psycopg2
import sys



class ConnectionDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):

        QtWidgets.QDialog.__init__(self)
        self.dialog_window = loadUi("dialog.ui")
        self.buttonBox = self.dialog_window.buttonBox
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.reject)
        self.conn_string = ""



    def apply(self):
        conn_string = str("host='"+self.dialog_window.lineEdit_5.text()+"' dbname='"+self.dialog_window.lineEdit_6.text()+"' user='"+self.dialog_window.lineEdit_7.text()+"' password='"+self.dialog_window.lineEdit_9.text()+"'")

        if self.test_connection(conn_string):
            self.conn_string = conn_string




        else:
            QMessageBox.information(self.dialog_window, 'INFO', "Please check the connection data or existence of database.",
                                 QMessageBox.Ok)
            self.dialog_window.show()


    def reject(self):
        sys.exit()

    def test_connection(self,conn_string):
        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.close()
            conn.close()
            return True
        except Exception :
            QMessageBox.critical(self.dialog_window, 'ERROR', "Error during connection to database.",
                                 QMessageBox.Ok)
            return False




class DdWindow( QtWidgets.QMainWindow):

    def __init__(self, cn_string, parent=None):
        self.flag = True
        self.choosen_schema = None
        self.choosen_table = None
        QtWidgets.QMainWindow.__init__(self)
        self.init_connection(cn_string)
        self.main_window = loadUi("mwindow.ui")
        self.main_table = self.main_window.tableWidget
        self.add_button = self.main_window.add
        self.delete_button = self.main_window.my_delete
        self.search_button = self.main_window.search
        self.help_button = self.main_window.help
        self.table_chooser = self.main_window.table_chooser
        self.schema_chooser = self.main_window.schema_chooser

        self.init_schema_chooser(self.schema_chooser)
        self.init_table_chooser(self.table_chooser)
        # self.fill_table()



    def init_table_chooser(self,tb_chooser):

        self.cursor.execute(("SELECT TABLE_NAME  from information_schema.tables where table_schema= '{0}'").format(self.choosen_schema))


        table_names = [name[0] for name in self.cursor.fetchall()]
        if len(table_names) == 0:
            tb_chooser.addItem(str(None))
        else:
            for table in table_names:
                tb_chooser.addItem(table)



    def init_schema_chooser(self, sh_chooser):
        self.cursor.execute("select schema_name from information_schema.schemata where  schema_name !~ '^(pg_|sql_)'  AND  schema_name !~'information_schema';")
        schema_names = [name[0] for name in self.cursor.fetchall()]
        for schema in schema_names:
            sh_chooser.addItem(schema)

        self.choosen_schema = self.schema_chooser.currentText()

        # sh_chooser.activated.connect(self.init_table_chooser)

    def init_connection(self,conn_string):
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()


    def fill_table(self):
        # self.cursor.execute(("SELECT * FROM  {0}").format(self.table_names[1]))
        self.cursor.execute(("SELECT * FROM sc.{0}").format(self.table_names[0]))
        # self.cursor.execute(("select a.attname, format_type(a.atttypid, a.atttypmod) from pg_attribute a where attname = 'geog'"))
        print(self.cursor.description)
        # a = [elem for elem in self.cursor.fetchall()]
        # print( a)
        #
        # colnames = [desc[0] for desc in self.cursor.description]
        # print(colnames)
        #
        #
        #
        # self.main_table.setColumnCount(2)
        # self.main_table.insertRow(self.main_table.rowCount())
        #
        # newitem = QTableWidgetItem(str(a[0][0]))
        # print(a[0][0])
        # self.main_table.setItem(0, 0, newitem)
        # self.main_table.item(0, 0).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # newitem = QTableWidgetItem(a[0][1])
        # self.main_table.setItem(0, 1, newitem)
        # self.main_table.item(0, 1).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.main_table.setHorizontalHeaderLabels(colnames)
        #
        # # for n, meaning in  enumerate(a):
        # #     self.main_table.insertRow(self.main_table.rowCount())
        # #     print(n,"  ",meaning)
        # #     for m, item in enumerate(meaning):
        # #         print("\t",m, "  ", item)
        # #         newitem = QTableWidgetItem(item)
        # #         self.main_table.setItem(n, m, newitem)
        # #         self.main_table.item(n, m).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # print(self.main_table.item(0,0).text())






if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = DdWindows()
    # window.open()
    # window.show()
    app = QApplication(sys.argv)
    # test = ConnectionDialog()
    # test.dialog_window.exec_()
    # conn_string = "host='localhost'dbname='postgres' user='postgres' password='root'"
    conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"

    if conn_string!="":
        window = DdWindow(conn_string)
        window.main_window.show()
    sys.exit(app.exec_())

