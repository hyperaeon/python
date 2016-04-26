__author__ = 'hzliyong'

print(True + False + 42)

print(bool('I thind'))
print(bool(''))
print(bool(2))
print(bool(0))

number = int(input('Enter a number'))
if number <= 10 and number >= 1:
    print("Great!")
else:
    print("Wrong")

if 1 <= number <= 10:
    print("Great!")
else:
    print("Wrong")

age = 10
assert 0 < age < 100
