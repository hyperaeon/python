#!/usr/bin/python
# -*- coding: utf-8 -*-

import operator
__author__ = 'hzliyong'

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}

print(cmp(dict1, dict2))
print(cmp(dict2, dict3))
print(cmp(dict1, dict4))
