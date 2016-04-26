__author__ = 'hzliyong'


f = open('somefile.txt', 'w')
f.write('Hello, ')
f.write('world!')
f.close()


f = open("somefile.txt", "r")
str = f.read(4)
print(str)
str = f.read()
print(str)
f.close()
