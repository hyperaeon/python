__author__ = 'hzliyong'


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


# fibs = Fibs()
# for f in fibs:
#     if f > 1000:
#         print(f)
#         break

it = iter([1, 2, 3])
for i in it:
    print(i)


class TestIterator:
    value = 0

    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self

ti = TestIterator()
ls = list(ti)
print(ls)
