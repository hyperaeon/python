__author__ = 'hzliyong'

x = [1, 1, 1]
x[2] = 2
print(x)

names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]
print(names)

name = list('Perl')
name[2:] = list('ar')
print(name)

name = list('Perl')
name[1:] = list('ython')
print(name)