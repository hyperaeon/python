__author__ = 'hzliyong'


class MyClass:
    @staticmethod
    def smeth():
        print("This is a static method")

    @classmethod
    def cmeth(cls):
        print("THis is a clas method of", cls)

MyClass.smeth()
MyClass.cmeth()
