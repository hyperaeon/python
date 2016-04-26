#!/usr/bin/python

__author__ = 'hzliyong'

list1, list2 = [123, 'xyz'], [456, 'abc']
print(cmp(list1, list2))

list3 = list2 + [456]
print(list2, list3)