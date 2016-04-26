__author__ = 'hzliyong'


class A:
    def hello(self):
        print("Hello. I'm A.")


class B(A):
    def hello(self):
        print("Hello. I'm B")


a = A()
b = B()
a.hello()
b.hello()


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


b = Bird()
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        # super(SongBird, self).__init__
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()


