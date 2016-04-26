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
    'phone': 'phone number',
    'addr' : 'address'
}
name = str(input("name:"))
request = str(input('phone number (p) or address(a)?'))
key = request
if request == 'p' :
    key = 'phone'
elif request == 'a':
    key = 'addr'
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("%s's %s is %s." %(name,label, result))

d = {'title':'asdfasf', 'url': 'foasefsf'}
print(d.items())

it = d.__iter__()
print(list(it))

d = {'x':1, 'y':2}
print(d.pop('x'))
print(d)

d = {}
d.setdefault('name', 'N/A')
print(d)
d['name'] = 'Gumby'
d.setdefault('name', 'NA')
print(d)

d = {
    'title':'pheone',
    'url':'fasdfas'
}
x = {'title':'safasdfsdf'}
d.update(x)
print(d)
