import sys
from PyQt5 import QtWidgets, QtCore

class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        loginLayout = QtWidgets.QFormLayout()
        loginLayout.addRow("Username", self.username)
        loginLayout.addRow("Password", self.password)

        self.buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.check)
        self.buttons.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(loginLayout)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def check(self):
        if str(self.password.text()) == "12345": # do actual login check
            self.accept()
        else:
            pass # or inform the user about bad username/password


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)

    def setUsername(self, username):
        # do whatever you want with the username
        self.username = username
        self.label.setText("Username entered: %s" % self.username)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    login = LoginDialog()
    if not login.exec_(): # 'reject': user pressed 'Cancel', so quit
        sys.exit(-1)

    # 'accept': continue
    main = MainWindow()
    main.setUsername(login.username.text()) # get the username, and supply it to main window
    main.show()

    sys.exit(app.exec_())