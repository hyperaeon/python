#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

dict = {'Name': 'Zara', 'Age': 7}
print(dict)
dict2 = {'Age': 27, 'Sex': 'female'}
dict.update(dict2)
print(dict)

print(dict.values())