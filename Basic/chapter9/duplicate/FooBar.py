__author__ = 'hzliyong'


class FooBar:
    def __init__(self, value=42):
        self.somevar = value


foo = FooBar(33)
print(foo.somevar)


class A:
    def hello(self):
        print("Hello I'm A")


class B(A):
    pass


b = B()
b.hello()


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Eating")
            self.hungry = False
        else:
            print("No, thanks")


b = Bird()
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

s = SongBird()
s.sing()
s.eat()
