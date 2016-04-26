__author__ = 'hzliyong'

permission = 'rw'
if 'w' in permission:
    print(True)
else:
    print(False)

users = ['mlh', 'foo', 'bar']
input_name = input("Enter your name:")
if input_name in users:
    print(True)
else:
    print(False)

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
username = input('User name:')
pin = input('PIN code:')
if [username, pin] in database:
    print('Access granted')
