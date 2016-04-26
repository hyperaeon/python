__author__ = 'hzliyong'

# raise Exception
# raise ArithmeticError

try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus...')

except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't number, was it?")

class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


calculator = MuffledCalculator()
calculator.calc('10/2')
calculator.muffled = True
calculator.calc('10/0')
