import MySQLdb

def getSleep():
	conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
	cur=conn.cursor()
	conn.select_db('network')
	sql='select count(*) from task'
	cur.execute(sql)
	result=cur.fetchone()
	if result[0]==0:
		return None
	else
		sql='select ip from ips where work=0 and status=1'
		cur.execute(sql)
		result=cur.fetchall()
		if result==():
			return None
