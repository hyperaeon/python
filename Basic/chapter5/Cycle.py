__author__ = 'hzliyong'
x = 1
while x <= 100:
    print(x)
    x += 1

words = ['this','is', 'an', 'ex','parrot']
for word in words:
    print(word)


for num in range(1,10):
    print(num)

d = {'x':1, 'y':2, 'z':3}
for key in d:
    print(key,'Corresponds to',d[key])

for key,value in d.items():
    print(key,'Corresponds to',value)