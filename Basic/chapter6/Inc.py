__author__ = 'hzliyong'


def inc(x):
    return x + 1


def inc2(x):
    x[0] = x[0] + 1


foo = [10]
inc2(foo)
print(foo)