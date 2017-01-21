#!/usr/bin/python3

import MySQLdb
import configparser

def mysql_exec(sql):
    """
    执行sql命令
    """
    #:获取配置信息
    path = 'mysql.ini'
    config = configparser.ConfigParser()
    config.read(path)
    host = config.get("Settings","host")
    user = config.get("Settings","user")
    passwd = config.get("Settings","passwd")
    port = config.get("Settings","port")

    #:连接数据库
    conn = MySQLdb.connect(host=host, user=user,passwd=passwd,port=int(port))
    cur = conn.cursor()
    conn.select_db('network')

    #执行sql命令
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    
    #:关闭数据库连接
    cur.close()
    conn.close()

    return result

if __name__ == '__main__':
    sql = 'select * from ips'
    for i in range(5):
        print(mysql_exec(sql)) 
