#coding:utf-8
import sys
import time
import subprocess
import answer
import mylog
'''
'''
i=0
port2 = 33332
port = 33333
flag = False
try:
    host = sys.argv[1]
except IndexError as e:
    mylog.error_log(e,'short of index')
    exit(1)

while True:
    data = answer.send(host,port,'join')
    if data == 'error':
        mylog.log('connect is failed','0')
        flag = False
        break
    if data == 'done':
        print('done')
        if flag:
            timeend = time.time()
            tm = timeend - timestart
            print(tm)
            flag = False
        time.sleep(5)
        continue
    if not flag :
        timestart = time.time()
    print(data)
    flag = True
    msg = data.split('&')
    run = msg[0]
    ids = msg[1]
    (status,output) = subprocess.getstatusoutput(run)
    get = answer.send(host,port2,output + '&' + ids)
    '''if get == 'success':
        mylog.log(get,ids)
    else:
        mylog.log(get,ids)
    '''
    mylog.log(get,ids)
