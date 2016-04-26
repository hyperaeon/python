__author__ = 'hzliyong'


items = [('name','Gumby'),('age',42)]
d = dict(items)
print(d)
print(d['name'])

d = dict(name='Gumby',age=42)
print(d['age'])

x = {}
x[42]='FooBar'
print(x)