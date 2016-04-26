__author__ = 'hzliyong'

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

return_value = d.clear()
print(d)
print(return_value)

x = {}
y = x
x['key'] = 'value'
print(y)
x = {}
print(y)

x = {}
y = x
x['key'] = 'value'
print(y)
x.clear()
print(y)

x = {'username' : 'admin', 'machines' : ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

from copy import deepcopy
d = {}
d['name'] = ['alfred', 'betreand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)

fromk = {}.fromkeys(['name','age'])
print(fromk)

fromdict = dict.fromkeys(['name', 'age'])
print(fromdict)

d = {}
print(d.get('name', 'N/A'))
d['name'] = 'eowe'
print(d.get('name'))