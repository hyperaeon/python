__author__ = 'hzliyong'

import fileinput

filename = 'somefile.txt'


def process(string):
    print("Processing: ", string)


for line in fileinput.input(filename):
    process(line)

f = open(filename)
for line in f:
    process(line)
f.close()