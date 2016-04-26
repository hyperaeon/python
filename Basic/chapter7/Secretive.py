__author__ = 'hzliyong'


class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is: ")
        self.__inaccessible()


s = Secretive()
s.accessible()
s._Secretive__inaccessible()


def foo(x):
    return x * x


foo = lambda x: x * x
