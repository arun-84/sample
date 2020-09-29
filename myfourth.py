# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtSamples\myfourth.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1146, 820)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 451, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(520, 50, 351, 51))
        self.label_2.setObjectName("label_2")
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setGeometry(QtCore.QRect(36, 380, 451, 71))
        self.labelSelected.setText("")
        self.labelSelected.setObjectName("labelSelected")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 151, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonMedium = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.verticalLayout.addWidget(self.radioButtonMedium)
        self.radioButtonLarge = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout.addWidget(self.radioButtonLarge)
        self.radioButtonXLarge = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonXLarge.setObjectName("radioButtonXLarge")
        self.verticalLayout.addWidget(self.radioButtonXLarge)
        self.radioButtonXXLarge = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonXXLarge.setObjectName("radioButtonXXLarge")
        self.verticalLayout.addWidget(self.radioButtonXXLarge)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 140, 160, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonCreditCard = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonCreditCard.setObjectName("radioButtonCreditCard")
        self.verticalLayout_2.addWidget(self.radioButtonCreditCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout_2.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout_2.addWidget(self.radioButtonCashOnDelivery)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Choose your Shirt Size</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Choose your Payment Mode</span></p></body></html>"))
        self.radioButtonMedium.setText(_translate("Dialog", "Medium"))
        self.radioButtonLarge.setText(_translate("Dialog", "Large"))
        self.radioButtonXLarge.setText(_translate("Dialog", "X-Large"))
        self.radioButtonXXLarge.setText(_translate("Dialog", "XX-Large"))
        self.radioButtonCreditCard.setText(_translate("Dialog", "Credit Card"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "Net Banking"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Cash on Delivery"))

