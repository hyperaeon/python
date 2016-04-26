__author__ = 'hzliyong'
from random import choice


def getPrice(object):
    if isinstance(object, tuple):
        return object[1]
    elif isinstance(object, dict):
        return int(object['price'])
    else:
        return magic_network_method(object)


def magic_network_method(object):
    return None;


x = choice(['Hello, world!', [1, 2, 'e', 'e', 4]])
print(x.count('e'))


def add(object, object1):
    return object + object1


print(add(1, 3))
print(add('2', '2'))
