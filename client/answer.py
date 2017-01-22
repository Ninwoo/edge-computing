#!/usr/bin/python
#coding=utf-8
import socket
import subprocess
import re

def send(host,port,msg):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    #:使用ping检测网络能否到达
    cmd='ping -w 1 -c 1 '+host
    (status,output)=subprocess.getstatusoutput(cmd)
    regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
    if len(regex.findall(output))>0:
        #:发送消息
        s.connect((host,port))
        s.send(msg)
        data=s.recv(1024)
        s.close()
        #:返回得到的消息
        return data
