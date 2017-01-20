import MySQLdb

def add(ip):
	try:
		conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
		cur=conn.cursor()
		conn.select_db('network')
		sql='select id from ips where ip="'+ip+'"'
		cur.execute(sql)
		result=cur.fetchone()
		if result==None:
			sql='insert into ips(ip,work,status)values("'+ip+'",0,1)'
			cur.execute(sql)
			conn.commit()
		else:
			sql='update ips set status=1 where ip="'+ip+'"'
			cur.execute(sql)
		return True
	except MySQLdb.Error,e:
			print "Mysql Error%d:%s"% (e.args[0],e.args[1])
			return False
