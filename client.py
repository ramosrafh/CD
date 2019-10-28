# TRABALHO DE COMUNICAÇÃO DE DADOS


import socket
import os
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi



class EditarEvento(QDialog):
    def __init__(self):
        super(EditarEvento, self).__init__()
        loadUi('client.ui', self)
        self.executar()

    def executar(self):
        self.b_editar.clicked.connect(self.editar_evento)
        self.b_editar.clicked.connect(self.close)





class Comunicate(QDialog):

    def __init__(self):
        super(EditarEvento, self).__init__()
        loadUi('editar_evento.ui', self)
        self.executar()

    def executar(self):
        self.b_editar.clicked.connect(self.editar_evento)
        self.b_editar.clicked.connect(self.close)


    ### THE CODE

    def message(self):
        msg = input("Type the message here: ")

        return msg

    def msg2bin(self, msg):
        conv = msg.encode('utf8')
        #conv = ' '.join(format(ord(x), 'b') for x in msg)

        return conv

    def msg2array(self, msg):
        conv = ' '.join(format(ord(x), 'b') for x in msg)
        # print(conv)
        return conv

    # def nrz():


s = socket.socket()
host = socket.gethostname()
port = 1233


com = Comunicate()


msg = com.message()
conv = com.msg2bin(msg)

test = com.msg2array(msg)
array = []

for i in test:
    array.append(i)

# print(array)

s.connect((host, port))
s.send(conv)
