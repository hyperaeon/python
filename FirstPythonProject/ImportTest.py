__author__ = 'hzliyong'
# import Support
from Support import print_func
# Support.print_func("asdf")
print_func("yes")

money = 2000
def addMoney():
    global money
    money = money + 1
    return money
print(addMoney())