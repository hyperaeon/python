__author__ = 'hzliyong'


# def foo(x):
#     return x * x


foo = lambda x: x * x
print(foo(3))


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
print(m1.members)

m2 = MemberCounter()
m2.init()
print(m2.members)