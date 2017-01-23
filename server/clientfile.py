#!/usr/bin/python
#coding:utf-8
import socket
import sys
import time
port=60001
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def recvfile(filename,name):
    print("server ready,now client rece file~~")
    (file,type)=filename.split('.')
    f=open(name+'.'+type,'wb')
    while True:
        data=s.recv(4096)
        if data=='EOF'.encode():
            print("recv file success")
            break
        f.write(data)
    f.close()
def sendfile(filename):
    print("server ready,now client sending file~~")
    f=open(filename,'rb')
    while True:
        data=f.read(4096)
        if not data:
            break
        s.sendall(data)
    f.close()
    time.sleep(1)
    s.sendall('EOF'.encode())
    print("send file success!")

def confirm(s,client_command):
    s.send(client_command.encode())
    data=s.recv(4096).decode()
    print(data)
    if data=='ready':
        return True

try:
    if len(sys.argv)==1:
        print("need argv")
    else:
        ip=sys.argv[1]
        action=sys.argv[2]
        filename=sys.argv[3]
        name=sys.argv[4]
        s.connect((ip,port))
        client_command=action+' '+filename
        if action=='get':
            if confirm(s,client_command):
                recvfile(filename,name)
            else:
                print("server get error!")
        elif action=='put':
            if confirm(s,client_command):
                sendfile(filename)
            else:
                print("server get error!")
        else:
            print("command error!")
except socket.error as e:
    print("get error as")
finally:
    s.close()
