__author__ = 'hzliyong'


def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
                print("after yield")
    except TypeError:
        yield nested


print(list(flatten([1, 2, 3, [2, 3], 3, 3, [23, 3, 3, [3, [3, 3]]]])))


def flattern2(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        for sublist in nested:
            for element in flattern2(sublist):
                yield element
    except TypeError:
        yield nested


# print(list(flattern2(['foo', ['bar', ['baz']]])))


def test(r):
    try:
        l = r + ''
        print(l)
    except TypeError:
        print("TypeError")


r = ['foo']
test(r)
