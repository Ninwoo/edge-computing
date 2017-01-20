#listening the port you give
#if the message got from slave is join,execute task.py and then print working
#else print error

import socket
import sys
import checkstatus
import commands
import MySQLdb
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

if len(sys.argv)==1:
	print "need argv"
else:
	host=''
	port=int(sys.argv[1])
	s.bind((host,port))
	s.listen(3)
	while True:
		client,ipaddr=s.accept()
		ip=str(ipaddr[0])
		data=client.recv(1024)
		if data=='join':
			(status,output)=commands.getstatusoutput('python task.py '+ip)
			out=output
			#send the output to slave through the tcp socket 
			print 'working'
		else:
			out='error'
			print 'error'
		client.send(out)
		client.close()

