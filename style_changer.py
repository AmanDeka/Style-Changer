from PyQt5 import QtWidgets, uic
import sys


class StyleChanger(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = StyleChanger()
app.exec_()