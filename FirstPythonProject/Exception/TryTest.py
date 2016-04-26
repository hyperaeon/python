__author__ = 'hzliyong'

try:
    fo = open("test.txt","w")
    fo.write("write someting")
except IOError:
    print("Can't find file")
else:
    print("File write successfully")
    fo.close()
