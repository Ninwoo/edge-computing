#!/usr/bin/python 
#coding:utf-8 
import socketserver 
import subprocess 
import string 
import time 
import sys
import mylog

class MyTcpServer(socketserver.BaseRequestHandler): 
    def recvfile(self, filename): 
        mylog.log("starting reve file!",'recvfile')
        f = open(filename, 'wb') 
        self.request.send('ready'.encode()) 
        while True: 
            data = self.request.recv(4096) 
            if data == 'EOF'.encode(): 
                mylog.log("recv file success!",'recvfile')
                break
            f.write(data) 
        f.close() 
                                         
    def sendfile(self, filename): 
        mylog.log("starting send file!",'sendfile')
        self.request.send('ready'.encode()) 
        time.sleep(1) 
        f = open(filename, 'rb') 
        while True: 
            data = f.read(4096) 
            if not data: 
                break
            self.request.send(data) 
        f.close() 
        time.sleep(1) 
        self.request.send('EOF'.encode()) 
        mylog.log("send file success!",'sendfile')
                                     
    def handle(self): 
        mylog.log(self.client_address,'handle')
        while True: 
            try: 
                data = self.request.recv(4096).decode() 
                mylog.log("get data:"+data,'handle')    
                if not data: 
                    mylog.log("break the connection!",'data error')
                    break                
                else: 
                    action, filename = data.split() 
                    if action == "put": 
                        self.recvfile(filename) 
                    elif action == 'get': 
                        self.sendfile(filename)  
                    else: 
                        mylog.log("get error!",'get')
                        continue
            except Exception as e: 
                mylog.error_log(e,'Exception')
                                             
                                         
if __name__ == "__main__": 
    host = ''
    port = int(sys.argv[1])
    s = socketserver.ThreadingTCPServer((host,port), MyTcpServer) 
    s.serve_forever() 
