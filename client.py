from socket import *
host=''
port=7100
s=socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
	Message = raw_input('Send :')
	s.send(Message)
	Reply=s.recv(1024)
	print 'Received ',(Reply)

s.close()