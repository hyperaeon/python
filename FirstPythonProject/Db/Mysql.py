__author__ = 'hzliyong'

import MySQLdb

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version:%s",data)

db.close()