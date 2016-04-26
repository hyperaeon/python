__author__ = 'hzliyong'

x = 1
scope = vars()
print(scope['x'])
scope['x'] += 1
print(scope['x'])

param = 'berry'


def combine(param):
    print(param + globals()['param'])


combine('Urb ')

x = 1


def change_global():
    global x
    x += 1


change_global()
print(x)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
