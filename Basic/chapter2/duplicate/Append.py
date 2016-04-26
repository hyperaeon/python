__author__ = 'hzliyong'

lst = list('123')
lst.append(4)
print(lst)

lt = ['to', 'too', 'to']
print(lt.count('to'))

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)

knights = ['leo', 'crem','leo']
print(knights.index('leo'))

numbers = [1,2,3,4,5]
numbers.insert(3,'four')
print(numbers)

print(numbers.pop())
print(numbers.pop(0))
print(numbers)

x = ['to','to']
print(x.remove('to'))
print(x)

x = [1, 2, 3]
x.reverse()
print(x)

x = [1, 2, 3]
list(reversed(x))

x = [1, 4, 3, 4, 5]
print(x.sort())
print(x)

x = [1, 4, -4, 55]
y = x[:]
y.sort()
print(y)
print(x)

numbers = [5, 2, 9, 7]
print(numbers)

x = ['a', 'bb', 'ccc', 'a', 'd']
x.sort(key=len)
print(x)
x.sort(reverse=True)
print(x)

print((423,32))

print(3*(32+3,))

print(tuple([3,2,3]))
print(tuple('abx'))