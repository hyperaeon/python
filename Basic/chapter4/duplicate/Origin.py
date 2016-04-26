__author__ = 'hzliyong'

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
numbers = ['2341', '9102', '3932', '2323', '3928']

print(numbers[names.index('Alice')])

phonebook = {'Alice': '32341', 'Beth': '3839', 'Cecil': '3923', 'Alice': '33332'}
print(phonebook['Alice'])

items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])

d = dict(name='Gumby', age=42)
print(d)
if 'name' in d.keys():
    print(True)
del d['name']
print(d)

x = [None] * 43
x[42] = 'Goe'
print(x)

x = {}
x[42] = 'Foobar'
print(x)
