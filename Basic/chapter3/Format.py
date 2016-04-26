__author__ = 'hzliyong'
from math import pi
from string import Template

format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

floatNumber = "Pi with three decimals: %.3f"
print(floatNumber % 3.142)

s = Template('$x. glorious $x!')
print(s.substitute(x='slurm'))

s = Template("make $$ selling $x")
print(s.substitute(x='slurm'))

s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))
