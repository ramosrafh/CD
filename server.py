import os
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()  # Get local machine name
port = 1233

s.bind((host, port))
s.listen(5)


client_socket, address = s.accept()
print("Conencted to - ", address, "\n")

data = client_socket.recv(2048)
dec = data.decode('utf8')
#my_bytes = bytearray(data)
print(dec)


print("The following data was received - ", data)
