# TRABALHO DE COMUNICAÇÃO DE DADOS


import socket
import os
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Server(QDialog):

    def __init__(self):
        super(Server, self).__init__()
        loadUi('server.ui', self)
        self.executar()

    def executar(self):
        self.receive()


    ### THE CODE

    def receive(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = socket.gethostname()  # Get local machine name
        port = 1333

        s.bind((host, port))
        s.listen(5)

        client_socket, address = s.accept()
        
        while True:
            data = client_socket.recv(2048)
            dec = data.decode('utf8')
            cri = self.decript(dec)
            print("decriii", cri)
            #my_bytes = bytearray(data)
            print(dec)

            self.message.setText(cri)


        print("The following data was received - ", data)
                
    def decript(self, msg):
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        criptografia = ''
        for x in msg:
            pos = alfabeto.find(x)
            new_pos = (pos-5) % 26
            criptografia+=alfabeto[new_pos]
        print(criptografia)
        return criptografia


app = QApplication(sys.argv)
widget = Server()
widget.show()   
sys.exit(app.exec_())













