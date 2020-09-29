# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtSamples\mythird.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 385)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 331, 71))
        self.label.setObjectName("label")
        self.radioButtonBeating = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBeating.setGeometry(QtCore.QRect(140, 120, 151, 41))
        self.radioButtonBeating.setObjectName("radioButtonBeating")
        self.radioButtonMainModule = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMainModule.setGeometry(QtCore.QRect(140, 160, 241, 41))
        self.radioButtonMainModule.setObjectName("radioButtonMainModule")
        self.radioButtonTopModule = QtWidgets.QRadioButton(Dialog)
        self.radioButtonTopModule.setGeometry(QtCore.QRect(140, 200, 131, 41))
        self.radioButtonTopModule.setObjectName("radioButtonTopModule")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(90, 240, 241, 51))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt;\">DEBUG</span></p></body></html>"))
        self.radioButtonBeating.setText(_translate("Dialog", "Beating Module"))
        self.radioButtonMainModule.setText(_translate("Dialog", "Main Module(cutting)"))
        self.radioButtonTopModule.setText(_translate("Dialog", "Top Module"))

