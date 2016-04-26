__author__ = 'hzliyong'
name = 'Ral'
if name == 'Ralph':
    print("Welcom")
elif name == 'Enid':
    pass
elif name == 'Bill':
    print('Access Denied')

scoundrel = {'age':42, 'first name':'Robin', 'last name':'of Locksley'}
robin = scoundrel
print(scoundrel)
print(robin)
scoundrel = None
print(robin)
robin = None
print(scoundrel)

x = 1
y = x
del x
print(y)

print(exec(print('Hello, world')))