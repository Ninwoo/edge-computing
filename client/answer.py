#!/usr/bin/python
#coding=utf-8
import socket
import subprocess
import re
import mylog

'''
'''
def send(host,port,msg):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        mylog.error_log(e,'socket_error')
        data = 'error'
    try:
        port = int(port)
    except ValueError as e:
        mylog.error_log(e,'port')
        data = 'error' 
    cmd='ping -w 1 -c 1 '+host
    (status,output)=subprocess.getstatusoutput(cmd)
    regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
    if len(regex.findall(output))>0:
        try:
            s.connect((host,port))
        except socket.gaierror as e:
            mylog.error_log(e,'Address-related error')
            data = 'error'
        except socket.error as e:
            mylog.error_log(e,'connection error')
            data = 'error'
        try:
            s.send(msg.encode())
        except socket.error as e:
            mylog.error_log(e,"Error sending")
            data = 'error'
        try:
            data=s.recv(1024)
            data = data.decode()
        except socket.error as e:
            mylog_error(e,'Error receiving')
            data = 'error'
        finally:
            s.close()
            return data
