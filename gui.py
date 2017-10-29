
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets

import psycopg2
import sys



class ConnectionDialog(QtWidgets.QMainWindow):

    def __init__(self):
        self.dialog_window = loadUi("dialog.ui")
        self.buttonBox = self.dialog_window.buttonBox
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.reject)
        self.conn_string = ""
        self.dialog_window.show()


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




class DdWindow():

    def __init__(self,cn_string):
        self.init_connection(cn_string)
        self.main_window = loadUi("mwindow.ui")
        self.main_table = self.main_window.tableWidget
        self.add_button = self.main_window.add
        self.delete_button = self.main_window.my_delete
        self.search_button = self.main_window.search
        self.help_button = self.main_window.help
        self.table_chooser = self.main_window.table_chooser
        self.init_table_chooser(self.table_chooser)
        self.main_window.show()

    def init_table_chooser(self, tb_chooser):
        self.cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        table_names = [name[0] for name in self.cursor.fetchall()]
        for table in table_names:
            tb_chooser.addItem(table)

    def init_connection(self,conn_string):
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()








if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = DdWindows()
    # window.open()
    # window.show()
    app = QApplication(sys.argv)
    test = ConnectionDialog()
    conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"
    window = DdWindow(conn_string)

    sys.exit(app.exec_())

