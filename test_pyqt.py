from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication, QDialog

import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("untitled.ui")



# dial.setNotchesVisible(True)



dial = window.dial

lcdNumber = window.lcdNumber

progressbar = window.progressBar
def slider_changed():
    lcdNumber.display(dial.value())
    progressbar.setValue(dial.value())

dial.valueChanged.connect(slider_changed)





window.show()
sys.exit(app.exec_())