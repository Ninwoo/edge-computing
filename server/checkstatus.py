import MySQLdb

def check():
	try:
		conn=MySQLdb.connect(host='mysql',user='root',passwd='123456',port=3306)

		cur=conn.cursor()
		conn.select_db('network')
		sql='select status from work'
		cur.execute(sql)
		result=cur.fetchall()
		if result[0][0]==1:
			print 'step 1'
			return 1
		elif result[0][0]==2:
			print 'step 2'
			return 2
		else:
			print 'step 3'
			return 3
		cur.close()
		conn.close()
	except MySQLdb.Error,e:

		print "Mysql Error%d:%s"% (e.args[0],e.args[1])
def checkWork(ip):
        conn=MySQLdb.connect(host='123.206.77.218',user='root',passwd='123456',port=12306)
        cur=conn.cursor()
        conn.select_db('network')
        sql='select work from ips where ip="'+ip+'"'
        cur.execute(sql)
        result=cur.fetchone()
        if result[0]==1:
                return True
        else:
                return False

