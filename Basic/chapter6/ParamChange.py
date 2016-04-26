__author__ = 'hzliyong'


def change(n):
    n[0] = 'Mr. Gumby'

names = ['Mrs. Entity', 'Mrs. Thing']
change(names)
print(names)

n = names[:]
n[0] = 'MMMM'
print(n)

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}
me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]
print(storage['middle']['Lie'])