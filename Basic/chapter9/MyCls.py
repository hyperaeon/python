__author__ = 'hzliyong'


class MyClass:
    def smeth(self):
        print('This is a static method')

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of', cls)

    cmeth = classmethod(cmeth)
