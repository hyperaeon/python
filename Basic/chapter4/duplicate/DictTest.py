__author__ = 'hzliyong'

people = {
    'Alice': {
        'phone' : '2323',
        'addr' : 'Foo drive 23'
    },
    'Beth' : {
        'phone' : '9102',
        'addr' : 'Bar street 32'
    },
    'Cecil' : {
        'phone' : '3158',
        'addr' : 'Baz avenue 90'
    }
}

labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = str(input('Name:'))
request = str(input('Phone number (p) or address (a)'))
if request == 'p' :
    key = 'phone'
elif request == 'a' :
    key = 'addr'
if name in people :
    print("%s's %s is %s." % (name, labels[key], people[name][key]))

phonebook = {'Beth': '39023', 'Cecil' : '2323'}
print("Cecil's number is %(Cecil)s" % phonebook)