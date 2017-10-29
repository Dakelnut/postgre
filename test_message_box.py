import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
# from PyQt5.QtWidget import QIcon
# from PyQt5.QtCore import pyqtSlot


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 messagebox - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
#         self.initUI()
# 
#     def initUI(self):
#         # self.setWindowTitle(self.title)
#         # self.setGeometry(self.left, self.top, self.width, self.height)
#         msg = QMessageBox(self)
#         msg.setIcon(QMessageBox.Information)
#         msg.setText("Please check the connection data or existence of database.")
#         msg.setWindowTitle("Info")
#         msg.setStandardButtons(QMessageBox.Ok)
#         buttonReply = QMessageBox.critical(self, 'ERROR', "Error during connection to database.",
#                                            QMessageBox.Ok)
# 
# 
#         self.show()
# 
# 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('ShowTime!', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)
        self._dialog = None

    def handleButton(self):
        if self._dialog is None:
            self._dialog = QtWidgets.QMessageBox(self)
            self._dialog.setWindowTitle('Messages')
            self._dialog.setModal(False)
            pos = self.pos()
            pos.setX(pos.x() + self.width() + 10)
            self._dialog.move(pos)
        self._dialog.setText(
            'The time is: %s' % QtCore.QTime.currentTime().toString())
        self._dialog.show()

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())