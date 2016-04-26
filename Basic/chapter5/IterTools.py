__author__ = 'hzliyong'
names = ['anne', 'eth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

comp = zip(names, ages)
for name, age in comp:
    print(name, 'is', age, 'years old')

strings = ['a', 'b', 'c']
for index, string in enumerate(strings):
    if 'a' in string:
        strings[index] = '[Censored]'
print(strings)

list = [4, 3, 6, 8, 3]
sortedList = sorted(list)
print(list)
print(sortedList)

he = 'Hello, world'
reversedList = reversed(he)
print(he)
# print(list(reversedList))
print(''.join(reversedList))
print(''.join(reversed('Hello, world!')))

for i in range(0, 10, 2):
    print(i)