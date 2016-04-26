#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print(str(dict))

dict = dict.fromkeys(seq, 10)
print(str(dict))

