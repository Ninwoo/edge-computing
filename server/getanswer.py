import socket
import sys
import checkstatus
import commands
import MySQLdb
import makefile
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#open the port 10413 for getting the answer from slave
if len(sys.argv)==1:
	print "need argv"
else:
	host=''
	port=int(sys.argv[1])
	s.bind((host,port))
	s.listen(3)
	while True:
		client,ipaddr=s.accept()
		ip=str(ipaddr[0])
		data=client.recv(1024)
		msg=data.split('&')
		id=msg[1]
		answer=msg[0]
		conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
		cur=conn.cursor()
		conn.select_db('network')
		#update the status of the task item by the id
		sql='update task set ends=1 where id='+id
		cur.execute(sql)
		conn.commit()
		cur.close()
		conn.close()
		#save the answer to a file named by its command's id
		makefile.make(id,answer)
		client.send('success')
		client.close()

