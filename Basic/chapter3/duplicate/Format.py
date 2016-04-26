__author__ = 'hzliyong'
from math import pi
from string import Template

format = "Hello, %s, %s enough for ya?"
values = ('world','Hot')
print(format % values)

format = "Pi with three decimals: %.3f"
print(format % pi)

s = Template('$x, glorious $x!')
result = s.substitute(x='slurm')
print(result)

s = Template("It's ${x}tastic!")
print(s.substitute(x='slurm'))

s = Template("Make $$ selling $x!")
print(s.substitute(x='slurm'))

s = Template("A $thing must never $action")
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))


print('%e' % 23232323232323)

