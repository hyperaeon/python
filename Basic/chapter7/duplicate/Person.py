__author__ = 'hzliyong'

__metaclass__ = type


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world ! I'm %s" % self.name)


foo = Person()
bar = Person()
foo.setName("Luke")
bar.setName("Walker")
print(foo.getName())
print(bar.getName())
