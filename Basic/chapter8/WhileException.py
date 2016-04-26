__author__ = 'hzliyong'

while True:
    try:
        x = int(input('Enter ther first number:'))
        y = int(input('Enter your second number:'))
        value = x / y
        print('x/y is', value)
    except:
        print('Invalid input.')
    else:
        break

x = None
try:
    x = 1 / 0
finally:
    print('Cleaning up...')
    del x
