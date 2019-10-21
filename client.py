import socket
import os


# TRABALHO DE COMUNICAÇÃO DE DADOS


class Comunicate():

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
