#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

import calendar
import sys
from datetime import datetime, timedelta
import time

'''
加上days天
'''
def add_day(current_date, days=1, format='%Y-%m-%d'):
    current_time = datetime.strptime(current_date, format)#把current_date从字符串转成datetime类型
    print(type(current_time))
    step = timedelta(days=days)#指定天数以便加减
    print(type(step))
    result_time = current_time + step#新增step天，step可以为负数
    print(type(result_time))
    return_time = result_time.strftime(format)#把result_time从datetime类型转化成字符串类型
    print(type(return_time))
    return return_time

'''
加上hours小时
'''
def add_hour(current_date, hours=1, format='%Y-%m-%d %H'):
    current_time = datetime.strptime(current_date, format)
    step = timedelta(hours=hours)
    result_time = current_time + step
    return result_time.strftime(format)

def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv[1:])

add_day('2016-02-29', 1)
print(add_hour('2016-02-29 20', 1))
print(time.strptime('2015-02-02 10', '%Y-%m-%d %H'))
print(time.mktime(time.strptime()))