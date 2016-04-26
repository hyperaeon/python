__author__ = 'hzliyong'

x = 1
scope = vars()
print(scope['x'])
scope['x'] += 1
print(x)

external = 'berry'


def combine(paramter):
    print(paramter + globals()['parameter'])


parameter = 'berry'
combine('sheof')
