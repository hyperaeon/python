__author__ = 'hzliyong'


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is ', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1 + 2 + 3')
tc.talk()
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
print(callable(getattr(tc, 'fnord', None)))
print(hasattr(getattr(tc, 'talk', None), '__call__'))
print(getattr(tc, 'name', None))
setattr(tc, 'name', "Oliver")
