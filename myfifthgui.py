# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:59:43 2020

@author: gr8ar
"""

from PyQt5.QtWidgets import QApplication,QDialog,QStyleFactory
import sys
from myfifth import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(QStyleFactory.keys())
        
        #QApplication.setStyle(QStyleFactory.create('Windows'))
        self.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyle('Windows')
    w=MyForm()
    w.show()
    sys.exit(app.exec_())