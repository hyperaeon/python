__author__ = 'hzliyong'
#coding:utf8


class Parent:
    def myMethod(self):
        print("父类方法")


class Child(Parent):
    def myMethod(self):
        print("子类方法")

c = Child()
c.myMethod()