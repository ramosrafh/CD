# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 502)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.w_events = QtWidgets.QWidget(Dialog)
        self.w_events.setGeometry(QtCore.QRect(10, 30, 441, 441))
        self.w_events.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.w_events.setObjectName("w_events")
        self.l_eventos = QtWidgets.QLabel(self.w_events)
        self.l_eventos.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.l_eventos.setStyleSheet("font: 57 17pt \"Ubuntu\";")
        self.l_eventos.setObjectName("l_eventos")
        self.label = QtWidgets.QLabel(self.w_events)
        self.label.setGeometry(QtCore.QRect(10, 50, 171, 21))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.w_events)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 80, 421, 311))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.w_events)
        self.pushButton.setGeometry(QtCore.QRect(160, 400, 101, 31))
        self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_eventos.setText(_translate("Dialog", "WhatsDados"))
        self.label.setText(_translate("Dialog", "Digite a sua mensagem:"))
        self.pushButton.setText(_translate("Dialog", "Enviar"))
