__author__ = 'hzliyong'

import cx_Oracle
# db=cx_Oracle.connect('paopao,'3axRQLt/ChVSnQ','172.17.11.38:1526:dapaopao')

conn=cx_Oracle.connect('jdbc:oracle:thin:@172.17.11.38:1526:dapaopao')
# c=conn.cursor()
# x=c.execute('select sysdate from dual')
# x.fetchone()
# c.close()
# conn.close()