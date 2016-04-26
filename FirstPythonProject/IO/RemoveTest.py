__author__ = 'hzliyong'
import os
create = open("new.txt","w")
create.close()
os.remove("new.txt")

os.mkdir("tests")
