import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6060))
s.sendall("test".encode())
data = s.recv(1024)
s.close()
print ('Received {}' .format(data))