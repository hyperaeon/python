__author__ = 'hzliyong'

__meta_class = type


class MyClass2:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method')


print(MyClass2.smeth())
print(MyClass2.cmeth())

d = {'name': "liyong", "age": 20}
for key, value in d.items():
    print(key, value)
print(d.keys())
