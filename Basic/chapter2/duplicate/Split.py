__author__ = 'hzliyong'

tag = '<a href = "http://www.xiupin.com"/>'
print(tag[9:20])
print(tag[9:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3: 6])
print(numbers[7: 10])
print(numbers[-3: 0])
print(numbers[-3:])
print(numbers[:])

print(numbers[0: 10: 1])
print(numbers[0: 10: 3])
print(numbers[::4])
print(numbers[::-1])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print('Hello, ' + 'World')

print('python' * 5)
sequence = [None] * 10
print(sequence)