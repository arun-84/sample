# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:53:54 2020

@author: gr8ar
"""

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from mythird import*
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonBeating.toggled.connect(self.dispModule)
        self.ui.radioButtonMainModule.toggled.connect(self.dispModule)
        self.ui.radioButtonTopModule.toggled.connect(self.dispModule)
        self.show()
    def dispModule(self):
        moduleSelected=""
        if self.ui.radioButtonBeating.isChecked()==True:
            moduleSelected="Beating Module"
        if self.ui.radioButtonMainModule.isChecked()==True:
            moduleSelected="Main Module"
        if self.ui.radioButtonTopModule.isChecked()==True:
            moduleSelected="Top Module"
        self.ui.labelResponse.setText(moduleSelected+" is selected")
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())