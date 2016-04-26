__author__ = 'hzliyong'

print('age', 42)

print(1, 2, 3)

import math as foobar
print(foobar.sqrt(4))

x, y, z = 1, 2, 3
print(x, y, z)
values = 1, 2, 3
print(values)

scoundrel = {'name': 'Robin', "girlfriend": "Marion"}
key, value = scoundrel.popitem()
print(key, value)

a, b, * rest = [1, 2, 3, 4]
print(rest)

print(bool(42))
print(bool(''))

name = str(input('What is your name:'))
if name.endswith("Gumby"):
    print("Hello, gumby")
else :
    print("hello, stranger")

