# TRABALHO DE COMUNICAÇÃO DE DADOS


import socket
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Client(QDialog):

    def __init__(self):
        super(Client, self).__init__()
        loadUi('client.ui', self)
        self.executar()

    def executar(self):
        self.b_enviar.clicked.connect(self.enviar)


    ### THE CODE

    def enviar(self):

        s = socket.socket()
        host = socket.gethostname()
        port = 1333

        msg = self.message()
        conv = self.msg2bin(msg)

        test = self.msg2array(msg)
        array = []

        for i in test:
            array.append(i)

        print(array)

        s.connect((host, port))
        s.send(conv)

        for i in array:
            if i == ' ':
                array.remove(i)

        input_amp = array
        plt.plot(input_amp, color='red', drawstyle='steps-pre')
        plt.title("Comunicação de Dados - Trabalho 2")
        plt.ylabel('Amplitude')
        plt.xlabel("Time")
        plt.savefig("waveform.png")
        plt.show()
        

    def message(self):

        msg = self.get_message.toPlainText()

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


app = QApplication(sys.argv)
widget = Client()
widget.show()
sys.exit(app.exec_())
