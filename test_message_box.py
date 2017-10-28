import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please check the connection data or existence of database.")
        msg.setWindowTitle("Info")
        msg.setStandardButtons(QMessageBox.Ok)
        buttonReply = QMessageBox.critical(self, 'ERROR', "Error during connection to database.",
                                           QMessageBox.Ok)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())