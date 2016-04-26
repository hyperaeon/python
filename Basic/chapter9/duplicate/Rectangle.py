__author__ = 'hzliyong'

__metalass__ = type


class Rectangele:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            # return self.__dict__[name]
            return AttributeError

r = Rectangele()
r.__setattr__('test', (12, 33))
print(r.__getattr__('test'))
