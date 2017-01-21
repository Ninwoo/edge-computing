#!/usr/bin/python
#coding:utf-8
import conn
def count():
    #:统计在线的ip数
    sql = 'select count(*) from ips where status=1'
    result = conn.mysql_execute(sql,'fetchone')
    return result[0]

if __name__ == '__main__':
    print(count())
