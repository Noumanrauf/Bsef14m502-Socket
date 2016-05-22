import socket
import sys
host=''
port=7100
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(10)
conn1, arr=sock.accept()
print "Connection is established ",arr[0],"at" ,arr[1]
conn2, arr1=sock.accept()
print "Connection is eestablished",arr1[0],"at",arr1[1]

while 1:
	data=conn1.recv(1024)
	conn2.send(data)
	data=conn2.recv(1024)
	conn1.send(data)
conn1.close()
conn2.close()
sock.close()