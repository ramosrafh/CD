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
        print("Conencted to - ", address, "\n")

        data = client_socket.recv(2048)
        dec = data.decode('utf8')
        #my_bytes = bytearray(data)
        print(dec)

        self.message.setText(dec)


        print("The following data was received - ", data)
                



app = QApplication(sys.argv)
widget = Server()
widget.show()
sys.exit(app.exec_())













