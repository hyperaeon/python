__author__ = 'hzliyong'


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2], [3, 4], [5]]
for i in flatten(nested):
    print(i)

print(list(flatten(nested)))

g = ((i + 2) ** 2 for i in range(2, 27))
print(g.__next__())


def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten2([2, [3, [3, [3, [3]]]]])))


def test(nested):
    for sublist in nested:
        yield sublist


print(list(test('abc')))


def flatten3(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested


for j in flatten3(3):
    print(j)


def errorTest(lst):
    try:
        lst + ''
    except TypeError:
        print("Type Error")


errorTest(33)
errorTest('ad')


def pr():
    print("print")


def yieldTest():
    str = None
    s = 'ab'
    yield str and s


print(list(yieldTest()))