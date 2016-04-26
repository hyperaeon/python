#coding:utf-8
__author__ = 'hzliyong'

import MySQLdb

def opendb():
    url = '10.120.154.151:6000'
    db = MySQLdb.connect(host='10.120.154.151', port=6000,  user='vstoremirr',passwd='mirrnvzh',db='vstore-mirr',charset='utf8')
    return db


def getTB_CMS_Business(db):
    cur = db.cursor()
    sql = '''select id,contactemail,contactname from TB_CMS_Business'''
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        print(d)


def getdata(db):
    cur = db.cursor()
    sql = "SELECT OrderId,CouponCode FROM TB_Promotion_CouponOrder where (CouponCode like 'H%' or CouponCode like 'LS%' or CouponCode='G3397' or CouponCode='S0153') and CreateTime>'2015-12-22 00:00:00'"
    cur.execute(sql)
    data1 = cur.fetchall()
    strs = ''
    for r in data1:
        x = 'OrderId=' + repr(r[0])[:-1]
        x +=  ' or '
        strs += x

    strs = strs[0:len(strs)-3]
    sql1 = "SELECT OrderId,CartRPrice from TB_Order_OrderForm where (" + strs
    sql1 += ")  and PayState=30"
    cur.execute(sql1)
    data2 = cur.fetchall()
    rst ={}
    print('使用券下单 %d' %len(data1))
    for x in data1:
        rst[x[0]]=[x[1]]

    print('使用券已付款 %d' %len(data2))
    for y in data2:
        rst[y[0]].append(y[1])

    sql2 = "select OrderId from TB_Order_ReturnPackage where (" + strs
    sql2 += ") and OrderPackageState <> 4 and OrderPackageState <> 8 and OrderPackageState <> 11 and OrderPackageState <> 21 and OrderPackageState <> 24"
    print(sql2)
    cur.execute(sql2)
    data3 = cur.fetchall()
    print("退货订单数%d" %len(data3))
    ##去除退订的订单
##    if(len(data3) > 0):
##        for tui in data3:
##            rst.pop(tui)
    return rst


def storeorigin(rst):
    tf = open("rst.txt", "w+")
    for x in rst.keys():
        if len(rst[x]) > 1 :
            tem='%d' %x
            line = tem + ',' + rst[x][0] +','+ str(rst[x][1]) +'\n'
            tf.write(line)
    tf.close()

def storeadded(rst):
    cov = {}
    for m in rst.keys():
        if len(rst[m]) > 1 :
            if(cov.has_key(rst[m][0])):
               cov[rst[m][0]] += rst[m][1]
            else:
               cov[rst[m][0]] = rst[m][1]
        else:
            print("未付款订单 %d %s" %(m,rst[m]))
    print('已付款员工数量%d'%len(cov))
    tf = open("rst-all.txt", "w+")
    for x in cov.keys():
            line = x + ',' + str(cov[x]) +'\n'
            tf.write(line)
    tf.close()

def closedb(db):
    try:
        db.close();
    except Exception,ex:
        print(ex)


def showdata(datarows):
    for row in datarows:
        print(row)


def main():
    db = opendb()
    getTB_CMS_Business(db)
    # data = getdata(db)
   # showdata(data)
    closedb(db)
    # storeorigin(data)
    # storeadded(data)


if __name__ == '__main__':
    main()

