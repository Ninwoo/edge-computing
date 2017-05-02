#!/usr/bin/python3
import socket
import sys
import subprocess
import MySQLdb
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

if len(sys.argv)==1:
	print("need argv")
else:
	host=''
	port=int(sys.argv[1])
	s.bind((host,port))
	s.listen(3)
	while True:
		client,ipaddr=s.accept()
		ip=str(ipaddr[0])
		data=client.recv(1024).decode()
		if data=='join':
			(status,output)=subprocess.getstatusoutput('python3 task.py '+ip)
			out=output
			#send the output to slave through the tcp socket 
			print('working')
		else:
			out='error'
			print('error')
		client.send(out.encode())
		client.close()

