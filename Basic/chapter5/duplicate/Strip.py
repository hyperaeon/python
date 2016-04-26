__author__ = 'hzliyong'
from math import sqrt

str = ''
print(str[:-1])

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Don't find it")


print([x*x for x in range(10)])

print([x*x for x in range(10) if x % 3 == 0])

print([(x,y) for x in range(3) for y in range(3)])

boys = ['chris','arnold','bob']
girls = ['alice', ' bernice', 'clarice']
print([b + '+' + g for b in boys for g in girls if b[0]==g[0]])

girl = 'alice'
letterGirls = {}
letterGirls.setdefault(girl[0], []).append(girl)
print(letterGirls)
