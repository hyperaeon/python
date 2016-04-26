__author__ = 'hzliyong'
#coding=utf8

print("中国")

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值：",sum(10, 20))
print("相加后的值：",sum(21,33))

def sums(arg1,arg2):
    total = arg1 + arg2;
    print("和：",total);
    return total

total = sums(323,333)
print(total)