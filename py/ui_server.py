# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
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
        self.recebida = QtWidgets.QLabel(self.w_events)
        self.recebida.setGeometry(QtCore.QRect(10, 50, 171, 21))
        self.recebida.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.recebida.setObjectName("recebida")
        self.message = QtWidgets.QLabel(self.w_events)
        self.message.setGeometry(QtCore.QRect(10, 80, 421, 351))
        self.message.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_eventos.setText(_translate("Dialog", "WhatsDados"))
        self.recebida.setText(_translate("Dialog", "Mensagem recebida:"))
