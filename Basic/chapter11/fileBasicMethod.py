__author__ = 'hzliyong'

f = open(r'somefile.txt')
print(f.read(7))
print(f.read(4))
f.close()

f = open(r'somefile.txt')
print(f.read())
f.close()

f = open(r'somefile.txt')
for i in range(3):
    print(str(i) + ":" + f.readline())
f.close()

import pprint

f = open(r'somefile.txt')
pprint.pprint(f.readlines())

f = open(r'somefile.txt', 'w')
f.write('this\n is no \n haiku')
f.close()

f = open(r'somefile.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a \n"
f = open(r'somefile.txt', 'w')
f.writelines(lines)
f.close()