__author__ = 'hzliyong'

__metaclass__ = type


class MyCass:
    def smeth():
        print('This is a static method')

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class metho of ', cls)

    cmeth = classmethod(cmeth)
