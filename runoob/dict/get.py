#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'hzliyong'

dict = {'Name': 'Zara', 'Age': 7}
print("value is: %s " % dict.get('Age'))
print("value is: %s " % dict.get('sex', 'Never'))