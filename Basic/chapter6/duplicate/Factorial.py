__author__ = 'hzliyong'


def factorial(n):
    result = n
    for i in range(1, n):
        result *= 1
    return result


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
