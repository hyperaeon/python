__author__ = 'hzliyong'

print('price of eggs : %d' % 42)

print('Hexadecimal price of eggs: %x' % 42)

from math import pi

print('PI :%f...' % pi)
print('Very inexact estimate of pi:%i' % pi)

print('%10f' % pi)

print('%10.2f' % pi)

print('%.2f' % pi)

print('%.*s' % (7, 'Guido van Rossum'))

print('%010.2f' % pi)

print('%-10.2f' % pi)

print('%-300.200f' % pi)

print(('% 5d' % 10) + '\n' + ('% 5d' % -10))