__author__ = 'hzliyong'

f = open('somefile.txt', 'w')
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()
lines = list(open(r'somefile.txt'))
print(lines)
first, second, third = lines
print(first)
print(second)
print(third)
