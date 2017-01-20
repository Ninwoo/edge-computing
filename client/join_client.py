#!/usr/bin/python
#coding=utf-8
import socket
import sys
import commands
import re
import time

def join(host,port):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

	cmd='ping -w 1 -c 1 '+host
	(status,output)=commands.getstatusoutput(cmd)
	regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
	if len(regex.findall(output))>0:
		s.connect((host,port))
	        s.send('join')
        	data=s.recv(1024)
		s.close()
		return data
