__author__ = 'hzliyong'


def func(x):
    return x.isanum()


seq = ['foo', 'x41', '?']
print(filter(func, seq))
