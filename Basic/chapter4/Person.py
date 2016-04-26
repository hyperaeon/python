__author__ = 'hzliyong'

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 22'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

lables = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name:')

request = input('Phone number (p) or address (a)?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people:
    print("%s's %s is %s." % (name, lables[key], people[name][key]))
