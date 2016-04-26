__author__ = 'hzliyong'
#coding:utf8

class Parent:
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setattr(self, attr):
        Parent.parentAttr = attr;

    def getattr(self):
        print("父类属性：",Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print("子类构造函数")

    def childMethod(self):
        print("调用子类方法")

c = Child()
c.childMethod()
c.parentMethod()
c.setattr(200)
c.getattr()
print("Is sub:",issubclass(Child,Parent))