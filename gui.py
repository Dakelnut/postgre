from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import psycopg2
import sys





class ConnectionDialog():

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




class DdWindows(QMainWindow):


    # def load(self,path_to_db):






if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = DdWindows()
    # window.open()
    # window.show()
    app = QApplication(sys.argv)
    # window = loadUi("dialog.ui")
    # window.show()
    test = ConnectionDialog()

