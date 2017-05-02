#coding:utf-8
'''
send file to different slave
'''
import socket
import commands
import sys
import time
import os
import MySQLdb
from multiprocessing import Process,Lock,Value

class Master:
	thrdlist=[]
	result=[]
	def send(self,ip,action,filename,rename,totlock):
		createCommand="python clientfile.py "+ip+" "+action+" "+filename+" "+rename
		(status,output)=commands.getstatusoutput(createCommand)
		print output
	
	def main(self,action,filename,rename):
		ipaddr=[]
		try:
			conn=MySQLdb.connect(host='10.0.9.20',user='root',passwd='123456', port=3306)
			cur=conn.cursor()
			conn.select_db('network')
			cur.execute('select ip from ips where status=1')
			results=cur.fetchall()
			if results==None:
				print 'no can be used'
			else:
				for ip in results:
					ipaddr.append(ip[0])
		except MySQLdb.Error,e:
			print "Mysql Error%d:%s"% (e.args[0],e.args[1])
		slave=len(ipaddr)
		if slave!=0:
			totlock=Lock()
			for i in range(slave):
				pr=Process(target=master.send,args=(ipaddr[i],action,filename,rename,totlock))
				master.thrdlist.append(pr)
				pr.start()
			for thrd in master.thrdlist:
				print('start join==========')
				thrd.join()
		else:
			print 'there is no slave!'
if __name__ == "__main__":
	master = Master()
	action=sys.argv[1]
	filename=sys.argv[2]
	rename=sys.argv[3]
	master.main(action,filename,rename)

