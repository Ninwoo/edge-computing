#!/usr/bin/python3
#coding:utf-8
import MySQLdb
import configparser

def mysql_execute(sql,flag):
    """
    """
    path = 'mysql.ini'
    config = configparser.ConfigParser()
    config.read(path)
    host = config.get("Settings","host")
    user = config.get("Settings","user")
    passwd = config.get("Settings","passwd")
    port = config.get("Settings","port")

    try:
        conn = MySQLdb.connect(host=host, user=user,passwd=passwd,port=int(port))
        cur = conn.cursor()
        conn.select_db('network')

        cur.execute(sql)

        if flag == 'fetchall':
            result = cur.fetchall()
        elif flag == 'fetchone':
            result = cur.fetchone()
        elif flag == 'commit':
            conn.commit()
            result = 'commit'
        else:
            result = 'Failed'
    except MySQLdb.Error as e:
        print("Mysql Error%d:%s" % (e.args[0],e.args[1]))
        result = 'Failed'
    finally:
    
        cur.close()
        conn.close()

        return result

if __name__ == '__main__':
    sql = 'select * from task'
    for i in range(5):
        print(mysql_execute(sql,'fetchone')) 
