# TRABALHO DE COMUNICAÇÃO DE DADOS


import socket
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

ALGORITMO = sys.argv[1]

class Client(QDialog):

    def __init__(self):
        super(Client, self).__init__()
        loadUi('client.ui', self)
        self.connect()
        self.executar()

    def executar(self):
        self.b_enviar.clicked.connect(self.enviar)


    ### THE CODE

    def connect(self):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = 1333
        print("Connecting to the host...")
        self.s.connect((self.host, self.port))

    def enviar(self):

        while True:
            msg = self.message()
            cri = self.cript(msg)
            conv = self.msg2bin(cri)

            print("criii", cri)

            if ALGORITMO == "nrz":
                array = self.nrz(msg)
            elif ALGORITMO == "rz":
                array = self.rz(msg)
            else:
                array = None

            self.s.send(conv)
            #self.s.close()

            self.graph(array)
        

    def message(self):

        msg = self.get_message.toPlainText()

        return msg

    def msg2bin(self, msg):
        conv = msg.encode('utf8')
        #conv = ' '.join(format(ord(x), 'b') for x in msg)

        return conv

    def nrz(self, msg):
        conv = ' '.join(format(ord(x), 'b') for x in msg)
        array = []
        for i in conv:
            array.append(i)
        for i in array:
            if i == ' ':
                array.remove(i)
        return array
    
    def rz(self, msg):
        conv = ' '.join(format(ord(x), 'b') for x in msg)
        array = []
        for i in conv:
            array.append(i)
        for i in array:
            if i == ' ':
                array.remove(i)
        
        new_array = []

        for i, item in enumerate(array):
            if item == '0':
                array[i] = '-1'
        
        for i in array:
            new_array.append(i)
            new_array.append(0)

        return new_array
    
    def cript(self, msg):
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        criptografia = ''
        for x in msg:
            pos = alfabeto.find(x)
            new_pos = (pos+5) % 26
            criptografia+=alfabeto[new_pos]
        return criptografia

    def graph(self, array):
        plt.plot(array, color='red', drawstyle='steps-pre')
        plt.title("Comunicação de Dados - Trabalho 2")
        plt.ylabel('Amplitude')
        plt.xlabel("Time")
        plt.gca().invert_yaxis()
        plt.savefig("waveform.png")
        plt.show()


app = QApplication(sys.argv)
widget = Client()
widget.show()
sys.exit(app.exec_())
