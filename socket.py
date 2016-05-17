import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("39.59.22.241",8000))
sock.listen(2)
(client,(ip,port))=sock.accept()
client.send("you have a Message ")

while True:

	Reply = client.recv(1024)

	print 'Received:', (Reply)

	Message = raw_input('Send:')

	s.send(Message)

	

s.close()

