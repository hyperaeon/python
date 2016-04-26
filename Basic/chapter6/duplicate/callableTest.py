__author__ = 'hzliyong'

import math

x = 1
y = math.sqrt
print(callable(x))
print(callable(y))


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fibs(10))


def square(x):
    'Calculates the square of the number x.'
    return x * x

print(square.__doc__)