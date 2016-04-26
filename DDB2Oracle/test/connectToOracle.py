__author__ = 'hzliyong'
import cx_Oracle

# db = cx_Oracle.connect('paopao', '3axRQLt/ChVSnQ', '172.17.11.38:1526/dapaopao')
# db1 = cx_Oracle.connect('paopao/3axRQLt/ChVSnQ@172.17.11.38:1526/dapaopao')
# dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'XE')
# print dsn_tns
# db2 = cx_Oracle.connect('hr', 'hrpwd', dsn_tns)



print(cx_Oracle.clientversion())
username = "paopao"
passwd = "3axRQLt/ChVSnQ"
host = "172.17.11.38"
port = "1526"
sid = "dapaopao"

dsn = cx_Oracle.makedsn(host, port, sid)
print(dsn)

# connection = cx_Oracle.connect('username', 'passwd', dsn)
# connection = cx_Oracle.Connection("username/passwd@dsn")
conn = cx_Oracle.connect('username/passwd@dsn/sid')

cursor = conn.cursor()
# cursor = connection.Cursor()
cursor.execute("""
        select *
        from Vstore_log""")
for column_1, column_2, column_3 in cursor:
    print "Values:", column_1, column_2, column_3
