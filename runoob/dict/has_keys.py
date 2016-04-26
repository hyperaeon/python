#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

dict = {'Name': 'Zara', 'Age': 27}
print("value is: %s" % dict.keys())

print("Value is: %s " % dict.items())

for k, v in dict.items():
    print("Key: %s, Value: %s" % (k, v))


print("Value is: %s " % dict.setdefault('Name', None))
print("Value is: %s " % dict.setdefault('Sex', None))
