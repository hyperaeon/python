__author__ = 'hzliyong'

fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)


def fibs(num):
    result = [0, 1]
    for j in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fibs(8))


def square(x):
    """Calculates the square of the number x."""
    return x * x

print(square.__doc__)

print(help(square))
