#!/usr/bin/python


__author__ = 'hzliyong'

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print(list1[0])
print(list2[1:5])

list1[2] = 20001
print(list1)

del list1[2]
print(list1)

print(len(list1))
print(list1 + list2)

print(['Hi']*4)

print(1997 in list1)

for x in list2:
    print(x)