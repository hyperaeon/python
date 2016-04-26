__author__ = 'hzliyong'


# import exceptions



# raise Exception
# raise Exception("helolo")
# dir(exceptions)

class MuffledCalculator:
    muffled = False

    def cal(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

calculator = MuffledCalculator()
# print(calculator.cal("3 / 0"))
calculator.muffled = True
print(calculator.cal("3 / 0"))

class SomeCustomException(Exception):
    pass


try:
    x = input('Enter ther first number:')
    y = input('Enter the second number:')
    print(int(x) / int(y))
except ZeroDivisionError:
    print("The number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")
except ValueError:
    print("The value is not a number")s



