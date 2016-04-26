__author__ = 'hzliyong'

import sys

f = open(r'somefile.txt', 'w')
f.write('01234567890123456789')
f.seek(5)
f.write('Hello, python')
f.close()
f = open(r'somefile.txt')
print(f.read())
f.close()

f = open(r'somefile.txt')
f.read(3)
f.read(2)
print(f.tell())
