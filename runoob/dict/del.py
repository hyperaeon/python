#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

dict = {'Name': 'Area', 'Age': 7, 'Class': 'Alie'}
del dict['Name']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)