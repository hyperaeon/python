__author__ = 'hzliyong'
from math import pi
import string
s = '%s plus %s equals %s' % (1, 1, 2)
print(s)

p = 'Price of eggs: $%d' % 42
print(p)

p = 'Hexa decimal price of eggs: $%x' % 43
print(p)

p = 'Very inexact estimate of pi:%i' % pi
print(p)

pis = '%10f' % pi
print(pis)

pis = '%010.2f' % pi
print(pis)

pis = '%-10.2f' % pi
print(pis)

pis = '%+5d' % 10
print(pis)

print(string.digits)

str = 'with a moo and a moo and a moo'
print(str.find('moo'))

seq = ['1','2','3','4','5']
sep = '+'
print(sep.join(seq))