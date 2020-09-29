# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtSamples\myfirst.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1081, 899)
        self.labelresonse = QtWidgets.QLabel(Dialog)
        self.labelresonse.setGeometry(QtCore.QRect(140, 90, 131, 51))
        self.labelresonse.setObjectName("labelresonse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(240, 110, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(136, 210, 321, 20))
        self.label.setObjectName("label")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(410, 110, 75, 23))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelresonse.setText(_translate("Dialog", "Enter your name"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))

