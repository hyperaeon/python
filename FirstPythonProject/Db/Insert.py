__author__ = 'hzliyong'

import MySQLdb
userid = 'test123'
password = 'password'
db = MySQLdb.connect("localhost","testuser",'%s','%s') %(userid,password)
cursor = db.cursor()

sql = '''INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
    VALUES('Mac','Mohan',20,'M',2000)'''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()