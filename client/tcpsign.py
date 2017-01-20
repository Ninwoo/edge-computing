#!/usr/bin/python
#coding=utf-8
import socket
import sys
import commands
import re
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
host=sys.argv[1]
port=33334
while True:
        cmd='ping -w 1 -c 1 '+host
        (status,output)=commands.getstatusoutput(cmd)
        regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
        if len(regex.findall(output))>0:
                s.connect((host,port))
                s.send('sign')
                data=s.recv(1024)
                print "Reply from server ------%s" %data
		break
        else:
                continue

