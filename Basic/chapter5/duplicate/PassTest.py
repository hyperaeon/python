#coding=utf-8
__author__ = 'hzliyong'

import sys

name = ''
if name == 'a':
    print('a')
elif name == 'b':
    pass
print("pass")

x = 1
print(x)
del x
# print(x)

x = 1
y = x
del x
print(y)

script = "print('exec script')"
exec(script)

from math import sqrt
# print(exec ("sqrt = 1"))
print(sqrt(4))

scope = {}
exec("sqrt = 1") in scope
# print(sqrt(4))

def dealBoolean(record):
    for key, value in record.items():
        if value == True:
            record[key] = "True"
        if value == False:
            record[key] = "False"
    return record

def fixLine(line):
    if line.find('"true"') > 0:
       line = line.replace('"true"',':"true",')
    if line.find('"false"') > 0:
       line = line.replace('"false"',':"false",')
    # line = line.replace('true','"true"').replace('false','"false"')
    return line

json = '{"accountId":"","action":"page","browser":"Chrome","clientType":"web",' \
       '"cookie":"_da_ntes_uid=QcGSP"true"5hYWP8EjAmVoxl1;","deviceOs":' \
       '"Windows 7","deviceType":"Computer","fromPos":"","ip":"175.44.44.4",' \
       '"provinceCode":"35","robot":"0","time":"1449390542555","type":"homePage","typeName":"首页"}'
json = fixLine(json)
print(json)


print(eval('3 + 33'))

scope = {}
exec('x = 1') in scope
# print(eval('x*x', scope))
# print(eval(json))

csef = ('fsf',323)
print(csef)


