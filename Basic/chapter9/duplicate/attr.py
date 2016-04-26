__author__ = 'hzliyong'


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height


r = Rectangle()
r.width = 5
r.height = 10
print(r.getSize())
r.setSize((3, 5))
print(r.getSize())


class Rectangle2:
    __metaclass__ = type

    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

r = Rectangle2()
r.width = 10
r.height = 21
print(r.size)
r.size = (33,23)
print(r.size)