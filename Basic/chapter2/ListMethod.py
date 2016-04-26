__author__ = 'hzliyong'

lst = ['to', 'be', 'see', 'Be', 'to', 'be']
print(lst.count('to'))
print(lst.count('be'))

lst2 = ['23', '33']
lst.extend(lst2)
print(lst)

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

x = [1, 3, 5]
print(x.pop())
print(x)
print(x.pop(0))

y = ['a', 'b', 'c', 'd', 'a']
y.remove('a')
print(y)

z = [1, 3, 5]
z.reverse()
print(z)

e = list(reversed(z))
print(e)

s = [1,4,6,2,3,6,3,332,32,3]
m = s[:]
f = sorted(s)
s.sort()
print(s)
print(m)
print(f)

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)

x.sort(reverse=True)
print(x)


