__author__ = 'hzliyong'
#coding=utf8
def printme(str):
    print(str)
    return

def changeme(myList):
    myList.append([1,2,3,4]);
    print("函数内取值",myList);
    return

myList = [12,212,32];
changeme(myList);
print("函数外取值",myList)


printme("print me please")

def printinfo(name, age = 30):
    print("Name", name)
    print("Age",age)
    return

printinfo('Liyong', 29)

def printinfo(arg1,*vartuple):
    print("输出")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(19,332,33)


