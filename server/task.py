#coding:utf-8
import socket
import commands
import sys
import MySQLdb
import itselfip
import makefile
'''
build4.0
'''
ip=sys.argv[1]
flag=True
try:
        conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
       	cur=conn.cursor()
        conn.select_db('network')

	#get a command and its id(run$id) from task list,and update the status of tasklist
        sql='update task set gets=1,ip="'+ip+'",status=0 where gets=0 limit 1' 
        cur.execute(sql)
	conn.commit()
	sql='select id,runs from task where gets=1 and ends=0 and ip="'+ip+'"'
	cur.execute(sql)
        result=cur.fetchone()
        if result==None:
        	sql='update task set gets=1,ip="'+ip+'",status=0 where gets=1 and ends=0 and status=1 limit 1'
                cur.execute(sql)
		conn.commit()
		sql='select id,runs from task where gets=1 and ends=0 and ip="'+ip+'" limit 1'
		cur.execute(sql)
                result=cur.fetchall()
                if result==():
                	flag=False
			#if the tasklist is empty,print done
			print 'done'
                else:
			#start to do the task whick has been taken but not done.
                        id=result[0][0]
			run=result[0][1]
			#here print the command and id
			print run+'$'+str(id)
	else:
        	id=result[0]
                run=result[1]
		print run+'&'+str(id)

	cur.close()
        conn.close()

except MySQLdb.Error,e:
	print "Mysql Error%d:%s"% (e.args[0],e.args[1])

