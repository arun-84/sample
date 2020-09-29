# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:24:25 2020

@author: gr8ar
"""

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from mysecond import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.show()
    def dispFare(self):
        fare=0
        if self.ui.radioButtonBusinessClass.isChecked()==True:
            fare=1250
        if self.ui.radioButtonEconomyClass.isChecked()==True:
            fare=1000
        if self.ui.radioButtonFirstClass.isChecked()==True:
            fare=1500
        self.ui.labelFare.setText("Air Fare is "+str(fare))
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())
    
    
        
        