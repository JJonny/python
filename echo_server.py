from socket import *

host = 'localhost'
port = 1234

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((host, port))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()

    print('Server connected by', address)

    while True:
        data = connection.recv(1024)
        if not data:
            break

        if data == b'close':
            print('connection close')
            connection.close()
            break

        print(data)
        connection.send(b'Echo=>' + data)
connection.close()
sockobj.close()
print('socket closed')
