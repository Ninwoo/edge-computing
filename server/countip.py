#!/usr/bin/python
#coding:utf-8
import MySQLdb
def count():
	try:
		conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
		cur=conn.cursor()
		conn.select_db('network')
		cur.execute('select count(*) from ips where status=1')
		result=cur.fetchone()
		cur.close()
		conn.close()
		return result[0]
	except MySQLdb.Error,e:
		print "Mysql Error%d:%s"% (e.args[0],e.args[1])
		return 0
