__author__ = 'hzliyong'


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
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


storage = {}
init(storage)
print(storage)
me = 'Magnus Lie Hetland'
storage['first']['Lie'] = [me]
print(lookup(storage, 'first', 'Lie'))

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))
store(MyNames, 'Robin Hood')
print(lookup(MyNames, 'middle', ''))


def store2(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


d = {}
init(d)
store2(d, 'Han solo')
store2(d, 'Luke Skywalker', 'Anakin Skywalker')
lookup(d, 'last', 'Skywalker')
