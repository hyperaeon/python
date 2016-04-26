__author__ = 'hzliyong'


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
print(r.__next__())

for line in open("test.txt").readlines():
    print(line)


def fab(max):
    a, b = 0, 1
    while a < max:
        yield b
        a, b = b, a + b


for i in fab(20):
    print(i, ",")
