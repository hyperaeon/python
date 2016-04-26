__author__ = 'hzliyong'


class Secretive:
    def __inaccessible(self):
        print("bet you can't see me...")

    def accessible(self):
        print("the secret message is:")
        self.__inaccessible()


s = Secretive()
# s.__inaccessible()
s.accessible()
s._Secretive__inaccessible()
