#!/usr/bin/python
#coding=utf-8
import socket
import sys
import commands
import re
import time

def send(host,port,msg):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
	#judge the network status by ping
	cmd='ping -w 1 -c 1 '+host
	(status,output)=commands.getstatusoutput(cmd)
	regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
	if len(regex.findall(output))>0:
		s.connect((host,port))
	        s.send(msg)
        	data=s.recv(1024)
		s.close()
		return data
