__author__ = 'hzliyong'


x = None
try:
    x = 1/0
finally:
    print("cleaning..")
    del x


while True:
    try:
        x = input("First:")
        y = input("Second:")
        value = int(x) / int(y)
        print("x / y is ", value)
    except:
        print("Invalue input")
    else:
        break

