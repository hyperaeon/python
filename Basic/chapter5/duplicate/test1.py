__author__ = 'hzliyong'

items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)

d = {}
d['name'] = 'Gumby'
d['age'] = 41
print(d)
d.clear()
# print(d)


y = d.copy()

from copy import deepcopy

d = {}
d['name'] = ['alfred', 'bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('clive')
print(c)
print(dc)

e = {}.fromkeys(['name', 'age'])
print(e)

dict = {}.fromkeys(['name', 'age'], '(unknown)')
print(dict)

print(dict.get('name'))
print(d.get('age'))
print(d.pop('name'))

d.setdefault('name', 'NA')
print(d)

for key, value in dict.items():
    print(key, value)
