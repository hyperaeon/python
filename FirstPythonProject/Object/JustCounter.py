__author__ = 'hzliyong'
#coding:utf8


class JustCounter:
    __secretCount = 0;#私有变量
    publicCount = 0;#公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)
print(counter.__JustCounter__secretCount)
