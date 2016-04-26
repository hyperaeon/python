__author__ = 'hzliyong'

filename = 'somefile.txt'


def process(string):
    print("Processing : ", string)


f = open(filename)
char = f.read(1)
while char:
    process(char)
    char = f.read(1)
f.close()

f = open(filename)
while True:
    char = f.read(1)
    if not char:
        break
    process(char)
f.close()

f = open(filename)
while True:
    line = f.readline()
    if not line:
        break
    process(line)
f.close()