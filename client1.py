from socket import *
host =''
port =7100
s=socket(AF_INET,SOCK_STREAM)
s.connect((host,port))

while 1:
	Reply=s.recv(1024)
	print 'Received :' ,(Reply)
	mesg =raw_input("Answer")
	s.send(mesg)

s.close()