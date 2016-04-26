__author__ = 'hzliyong'

try:
    x = input('Enter your first number:')
    y = input('Enter your second number')
    print(x / y)
# except (ZeroDivisionError, TypeError) as e:
#     print(e)
except:
    print('Something wrong happend..')

try:
    print('A simple task')
except:
    print('What? something went wrong?')
else:
    print('Ah .. it went as planned')
