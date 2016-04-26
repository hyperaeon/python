__author__ = 'hzliyong'


def print_param(*params):
    print(params)


print_param('test', 2323)


def print_params(x, y, z=3, *params, **keypar):
    print(x, y, z)
    print(params)
    print(keypar)


print_params(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)
