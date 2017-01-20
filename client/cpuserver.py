#!/usr/bin/env python
#coding=utf-8
import socket
import sys,os
import commands
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
		print "Got a connect from %s"  %str(ipaddr)
		data=client.recv(1024)
		if data=='Cpu':
 			sy=os.popen('top -bi -n 2 -d 0.02').read().split('\n\n')[2].split('\n')[2].split(':')[1].split(',')[1]
			client.send(sy)
		else:
			client.send("echo:Failed!")
		client.close()
