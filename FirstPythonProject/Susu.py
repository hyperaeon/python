__author__ = 'hzliyong'
#_*_ coding=utf8 _*_
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not(i % j ):break
        j = j + 1
    if (j > i / j) :print("素数：",i)
    i = i + 1
print("结束")