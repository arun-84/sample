# -*- coding: utf-8 -*-

"""
Created on Fri Sep 18 16:48:33 2020

@author: gr8ar
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from myfirstui import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.label.setText("Hello "
        +self.ui.lineEditName.text())
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


