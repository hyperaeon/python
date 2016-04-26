__author__ = 'hzliyong'
from math import sqrt
for n in range(99, 80, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it")

for x in range(10):
    print(x*x)

print([x*x for x in range(10)])

girls = ['alice', 'bernice', 'clarice']
boys = ['chirs', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print(letterGirls)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])