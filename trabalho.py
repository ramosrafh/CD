# TRABALHO DE COMUNICAÇÃO DE DADOS

import matplotlib.pyplot as plt
import numpy as np


class Comunicate():

    def message(self):
        msg = input("Type the message here: ")

        return msg

    def msg2bin(self, msg):
        conv = ' '.join(format(ord(x), 'b') for x in msg)

        return conv

    def msg2array(self, msg):
        array = []
        conv = ' '.join(format(ord(x), 'b') for x in msg)

        for i in conv:
            array.append(i)

        return array
        # def nrz():


com = Comunicate()

msg = com.message()
conv = com.msg2bin(msg)


test = com.msg2array(msg)

print(test)

for i in test:
    if i == ' ':
        test.remove(i)
print(test)

input_amp = test
plt.plot(input_amp, color='red', drawstyle='steps-pre')
plt.title("Comunicação de Dados - Trabalho 2")
plt.ylabel('Amplitude')
plt.xlabel("Time")
plt.savefig("waveform.png")
plt.show()
