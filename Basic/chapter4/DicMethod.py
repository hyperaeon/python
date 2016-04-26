__author__ = 'hzliyong'
from copy import deepcopy

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

returned_value = d.clear()
print(d)

x = {}
y = x
x['name'] = 'Lio'
y = {}
y['name'] = 'OOO'
print(x)
print(y)

x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'charlar'
y['machines'].remove('bar')
print(x)
print(y)

z = deepcopy(x)
x['machines'].append('Cilve')
print(x)
print(z)

d = {}
print(d.get('name'))

d = {}
print(d.has_key('name'))
d['name'] = 'Gumbpy'
print(d.has_key('name'))