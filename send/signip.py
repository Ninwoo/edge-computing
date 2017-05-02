#coding:utf-8
import socket
import commands
import sys
import os
import MySQLdb
import divide
import itselfip
'''
'''
argv1=sys.argv[1]
argv2=sys.argv[2]
argv3=sys.argv[3]
argvs=argv3.split(" ")
list=[]
try:
	conn=MySQLdb.connect(host='mysql',user='root',passwd='123456',port=3306)
	cur=conn.cursor()
	conn.select_db('network')
	sql='update work set status=1'
	cur.execute(sql)
	conn.commit()
	output=divide.div(int(argvs[0]),int(argvs[1]))
	for arg in output:
		start=str(arg[0])
		end=str(arg[1])
		run=argv1+' '+argv2+' '+start+' '+end
		runs=(run,itselfip.get_local_ip("ethwe"))
		list.append(runs)
	sql="insert into task(gets,ends,status,runs,senders) values(0,0,0,%s,%s)"
	cur.executemany(sql,list)
	conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error%d:%s"% (e.args[0],e.args[1])

