__author__ = 'hzliyong'

import  os

file = open("test.txt","w")
file.write("Hello file system\n yes\n and \n")
print("File Name: " , file.name)
print("Close or not:", file.closed)
print("Opening mode:", file.mode)
# print("Softspace flag", file.softspace)
file.close()

fo = open("test.txt","r")
str = fo.read(10)
print("Read string is:",str)
po = fo.tell()
print("Current file position", po)

str = fo.read(10)
print("Before move read string is ", str)

po = fo.seek(0, 0)
str = fo.read(10)
print("Again read string is ", str)
fo.close()

os.rename("test.txt","renameTest.txt")

