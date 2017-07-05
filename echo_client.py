# import sys
from socket import socket, AF_INET, SOCK_STREAM

mess = str('close')
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect(('127.0.0.1', 1234))	
sockobj.send(mess.encode('utf-8'))

data = sockobj.recv(1024)
sockobj.close()	

print('Client received:', data)
