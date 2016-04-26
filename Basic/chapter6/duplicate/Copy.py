__author__ = 'hzliyong'


def change(n):
    n[0] = 'Mrs I'


names = ['Mr Right', 'Mrs Wrong']
change(names)
print(names)

n = names[:]
n[0] = 'sfe'
print(names)
print(n)

print(n is names)
print(n == names)