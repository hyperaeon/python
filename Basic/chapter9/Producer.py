__author__ = 'hzliyong'

nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


for num in flatten(nested):
    print(num)


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new


r = repeater(42)
print(r.__next__())


def flatten(nested):
    result = []
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
