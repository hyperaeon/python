
__author__ = 'hzliyong'

x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)

# name = str(input('what is your name?'))
name = 'd'
if 's' in name:
    print('Your name contains the letter s')
else:
    print('Your name not contains the letter s')
print('alpha' < 'beta')

print('Forl'.lower() == 'FoRl'.lower())
print([1,2] < [2, 1])

d = {}
d['a'] = ['b']
d['a'].append('c')
a = d.keys()
print(a)
