from PyQt5 import QtWidgets, uic
import sys
from styleformer import Styleformer
import torch
import warnings
warnings.filterwarnings("ignore")


class StyleChanger(QtWidgets.QMainWindow):
    def __init__(self):
        super(StyleChanger, self).__init__()
        uic.loadUi('app.ui', self)
        self.button.clicked.connect(self.show_style)
        self.sf1 = Styleformer(style = 0)
        self.sf2 = Styleformer(style = 1)  
        self.show()

    
    def show_style(self):
        self.recommender.clear()
        formal = self.sf1.transfer(self.textbox.toPlainText())
        informal = self.sf2.transfer(self.textbox.toPlainText())
        self.recommender.addItem("[Formal]"+formal)
        self.recommender.addItem("[Informal]"+informal)
 

app = QtWidgets.QApplication(sys.argv)
window = StyleChanger()
app.exec_()




