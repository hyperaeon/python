__author__ = 'hzliyong'

import chapter10.duplicate
import copy

print(chapter10.duplicate.PI)


list = [n for n in dir(copy) if not n.startswith("_")]
print(list)

list2 = [n for n in dir(copy)]
print(list2)
