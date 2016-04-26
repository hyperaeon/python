__author__ = 'hzliyong'


try :
    x = input("Enter a number")
    y = input("Enter a number too")
    print(int(x) / int(y))
except(ZeroDivisionError, TypeError, ValueError) as e:
    print("illegal value", e)
    print(e)

try :
    x = 39
    y = 23
except :
    print("wrong")
else:
    print("right")