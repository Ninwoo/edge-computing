import socket
import sys
import commands
import re
import time
import sys
import multiprocessing
import MySQLdb
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

def ping(ip):
	i=0
	while True:
		cmd='ping -w 1 -c 1 '+ip
		(status,output)=commands.getstatusoutput(cmd)
		regex=re.compile("time=\d*",re.IGNORECASE | re.MULTILINE)
		if len(regex.findall(output))>0:
			continue
		else:
			i=i+1
			if i>2:
				try:
					conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
					cur=conn.cursor()
					conn.select_db('network')
					cur.execute('select status from ips where ip="'+ip+'"')
					result=cur.fetchall()
					if result[0][0]==0:
						cur.execute('update task set status=1 where gets=1 and ends=0 and ip="'+ip+'"')
						conn.commit()
						cur.execute('update ips set work=0 where ip="'+ip+'"')
						conn.commit()
						cur.close()
						conn.close()
						print 'failed network!'
						break
					else:
						continue 
				except MySQLdb.Error,e:
					print "Mysql Error%d:%s"% (e.args[0],e.args[1])
	print 'failed'
	sys.exit(0)
					
def send(host,port,msg):
	try:
		s.connect((host,port))
		s.send(msg)
		data=s.recv(1024)
		print 'success&'+data
		s.close()
	except:
		print 'failed'
		conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
		cur=conn.cursor()
		conn.select_db('network')
		cur.execute('update task set status=1 where gets=1 and ends=0 and ip="'+ip+'"')
		conn.commit()
		cur.execute('update ips set status=0,work=0 where ip="'+host+'"')
		conn.commit()
		cur.close()
		conn.close()

if __name__=="__main__":
	host=sys.argv[1]
	port=int(sys.argv[2])
	msg=sys.argv[3]
	p1=multiprocessing.Process(target = ping, args = (host,))
	p2=multiprocessing.Process(target = send, args = (host,port,msg))

	p2.start()
	p1.start()
	
	while True:
		p=multiprocessing.active_children()
		if len(p)==1:
			cmd='kill -9 '+str(p[0].pid)
			(status,output)=commands.getstatusoutput(cmd)
			break	
		elif len(p)==2:
			continue
		else:
		
			break

