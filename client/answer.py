#!/usr/bin/python
#coding=utf-8
import socket
import subprocess
import re
import mylog

'''
socket 发送程序
'''
def send(host,port,msg):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        mylog.error_log(e,'socket_error')
        return False
    try:
        port = int(port)
    except ValueError as e:
        mylog.error_log(e,'port')
        return False
        #:使用ping检测网络能否到达
        cmd='ping -w 1 -c 1 '+host
        (status,output)=subprocess.getstatusoutput(cmd)
        regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
        if len(regex.findall(output))>0:
            #:发送消息
            try:
                s.connect((host,port))
            except socket.gaierror as e:
                mylog.error_log(e,'Address-related error')
                return False
            except socket.error as e:
                mylog.error_log(e,'connection error')
                return False
            try:
                s.send(msg.encode())
            except socket.error as e:
                mylog_error(e,"Error sending")
                return False
            try:
                data=s.recv(1024)
                #:返回得到的消息
                return data.decode()
            except socket.error as e:
                mylog_error(e,'Error receiving')
            finally:
                s.close()
