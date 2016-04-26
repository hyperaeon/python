__author__ = 'hzliyong'

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]
print(storage)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = ['first', 'middle', 'last']
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]




storage = {}
init(storage)
print(storage)
store(storage, 'Magus Lie Hetland')
print(lookup(storage, 'middle', 'Lie'))
store(storage, 'Li Yong')
print(lookup(storage, 'middle', ''))


def hello(greeting, name):
    print('%s, %s!' % (greeting, name))


hello(greeting='Hello', name='world')
hello(name='world', greeting='Hello')


def print_params(title, *params):
    print(title)
    print(params)


print_params('testing', 'name', 'jhon')


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)


def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


args = {'name': 'Mr. Right', 'age': 42}
print(with_stars(**args))
print(without_stars(args))
