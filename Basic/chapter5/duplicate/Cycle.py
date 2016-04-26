__author__ = 'hzliyong'


name = ''
while not name or name.isspace():
    # name = str(input("Please enter your name:"))
    name = 's'
print('Hello %s' % name)

words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

for number in range(0, 10):
    print(number)

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key)
b = d.items()
for a in b:
    print(a)

for key, value in d.items():
    print(key, value)

orderDic = {'29393': 'H32323', '3923': 'He2323'}
for key, value in orderDic.items():
    print(key, value)

names = ['leo', 'tom', 'jerry', 'betterman', 'corem']
ages = [22, 32, 33, 34, 23]
print(zip(names,ages))

for name, age in zip(names, ages):
    print(name, age)

strings = ['ab', 'cd', 'de']
for index, string in enumerate(strings):
    if 'ab' in string:
        strings[index] = 'dd'
print(strings)

ls = [4, 3, 6, 8, 3]
print(sorted(ls))
print(ls)