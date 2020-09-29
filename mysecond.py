# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtSamples\mysecond.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 251)
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(230, 60, 211, 18))
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(230, 80, 221, 18))
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(230, 100, 211, 16))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 291, 51))
        self.label.setObjectName("label")
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(130, 150, 221, 16))
        self.labelFare.setText("")
        self.labelFare.setObjectName("labelFare")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class"))
        self.label.setText(_translate("Dialog", "Choose the flight type"))

