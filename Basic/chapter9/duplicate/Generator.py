__author__ = 'hzliyong'

nested = [[1, 3], [3, 4], [5, 3]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


for num in flatten(nested):
    print(num)

print(list(flatten(nested)))

g = ((i + 2) ** 2 for i in range(2, 27))
print(g.__next__())
print(3 ** 3)
