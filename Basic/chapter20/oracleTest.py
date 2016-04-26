__author__ = 'hzliyong'

import cx_Oracle
conn=cx_Oracle.connect('/123456@172.17.11.38/ora11g')
c=conn.cursor()
x=c.execute('select sysdate from dual')
x.fetchone()
c.close()
conn.close()