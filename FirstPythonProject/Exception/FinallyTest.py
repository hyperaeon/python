__author__ = 'hzliyong'

try:
    fo = open("test.txt","w")
    fo.write("sdfowerfw")
finally:
    print("can't write ")
