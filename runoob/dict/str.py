#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

dict = {'Name': 'Alice', 'Age': 7}
print(str(dict))
print(dict)

print(type(dict))
dict2 = dict.copy()
print("dict2: %s" % dict2)

print(len(dict))
dict.clear()
print(len(dict))
print("dict2 after clear: %s " % dict2)
print("dict after clear: %s " % dict)

