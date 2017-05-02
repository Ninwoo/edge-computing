import time

def log(msg,taskid):
    msg = str(msg)
    print(time.asctime() + ':taskid:' + taskid +':'+msg)
def error_log(error,error_type):
    print("%s:%s:%s" % (time.asctime(),error_type,error))
 
