from select import select
from socket import socket, AF_INET, SOCK_STREAM


server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(('', 1234))
server_sock.setblocking(0)
server_sock.listen(10)

inputs = {server_sock}
outputs = {}
excepts = []

work = True
while work:
	input_ready, output_ready, except_ready = \
		select(list(inputs), outputs.keys(), excepts, 0.5)
	for s in input_ready:
		if s == server_sock:
			client_sock, address = server_sock.accept()
			client_sock.setblocking(0)
			inputs.add(client_sock)
		else:
			data = s.recv(1024)			
			if not data: 
				s.close()
			if data == b'close' or data == b'Close':				
				work = False
				break
			outputs[s] = data
			inputs.remove(s)

	for s in output_ready:
		if s in outputs:
			s.send(outputs[s])
			s.close()
