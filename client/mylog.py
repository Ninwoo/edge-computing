import time

#:输出log信息
def log(msg,taskid):
    print(time.asctime() + ':taskid:' + taskid +':'+msg)
#:输出错误log信息
def error_log(error,error_type):
    print(time.asctime() + ':' + error_type + ':' +error)
 
