# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 00:49:41 2020

@author: gr8ar
"""

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from myfourth import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.dispUser)
        self.ui.radioButtonLarge.toggled.connect(self.dispUser)
        self.ui.radioButtonXLarge.toggled.connect(self.dispUser)
        self.ui.radioButtonXXLarge.toggled.connect(self.dispUser)
        self.ui.radioButtonCreditCard.toggled.connect(self.dispUser)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispUser)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispUser)
        self.show()
    def dispUser(self):
        sizeSelected=""
        paymentSelected=""
        if self.ui.radioButtonMedium.isChecked()==True:
            sizeSelected="Medium"
        if self.ui.radioButtonLarge.isChecked()==True:
            sizeSelected="Large"
        if self.ui.radioButtonXLarge.isChecked()==True:
            sizeSelected="XL"
        if self.ui.radioButtonXXLarge.isChecked()==True:
            sizeSelected="XXL"
        if self.ui.radioButtonNetBanking.isChecked()==True:
            paymentSelected="Net Banking"
        if self.ui.radioButtonCreditCard.isChecked()==True:
            paymentSelected="Credit Card"
        if self.ui.radioButtonCashOnDelivery.isChecked()==True:
            paymentSelected="Cash on Delivery"
        self.ui.labelSelected.setText("Size Selected : "+ sizeSelected + "\nPayment Mode  :"+paymentSelected)
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())