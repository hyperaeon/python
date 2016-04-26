__author__ = 'hzliyong'

from random import choice

x = choice(['hello', [1, 2, 3, 'e']])
print(x.count('e'))