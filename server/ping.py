import MySQLdb
import os,sys,re
import subprocess
import time
while(True):
        time.sleep(5)
        try:
                conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
                cur=conn.cursor()
                conn.select_db('network')
                cur.execute('select ip,status from ips')
                result=cur.fetchall()
                if result==None:
                        print 'None'
                else:
                        for ip in result:
                                p=subprocess.Popen(["ping -w 1 -c 1 "+ip[0]],
                                                        stdin=subprocess.PIPE,
                                                        stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE,
                                                        shell=True)
                                out=p.stdout.read()
                                regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
                                if len(regex.findall(out))>0:
                                        print ip[0]+':Host Up!'
                                        if ip[1]!=1:
                                                cur.execute('update ips set status=1 where ip="'+ip[0]+'"')
                                                conn.commit()
                                else:
                                        print ip[0]+':Host Down!'
                                        if ip[1]!=0:
                                                cur.execute('update ips set status=0 where ip="'+ip[0]+'"')
                                                conn.commit()
                cur.close()
                conn.close()
        except MySQLdb.Error,e:  
                print "Mysql Error%d:%s"% (e.args[0],e.args[1])

