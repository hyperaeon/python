#coding=utf-8
__author__ = 'hzliyong'

import MySQLdb

'''
open ddb
'''
def opendb():
    host = '10.120.154.151'
    url = host + ':6000'
    db = MySQLdb.connect(host, port=6000, user='vstoremirr', passwd='mirrnvzh', db='vstore-mirr', charset='utf8')
    return db


'''
close ddb
'''
def closedb(db):
    try:
        db.close()
    except Exception, ex:
        print(ex)

'''
get data from ddb into tuple
'''
def getOrderFormFromDDB(db):
    cur = db.cursor()
    sql = '''select * from TB_Order_OrderForm  limit 100 offset 0'''
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        print(d)


def main():
    db = opendb()
    getOrderFormFromDDB(db)
    closedb(db)

if __name__ == '__main__':
    main()



