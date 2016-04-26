__author__ = 'hzliyong'

name = list('hello')
print(name)

name[2:] = list('sdd')
print(name)

del name[2]
print(name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:11:2])

lst = [1, 2, 3]
lst.append(4)
print(lst)
