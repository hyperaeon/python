__author__ = 'hzliyong'


text = 'With a moo-moo hear, and a moo-moo three'
print(text.find('moo'))


subject = '$$$Get rich now!!! %%%'
print(subject.find('$$$'))
print(subject.find('$$$', 1, 2))

seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

dirs = '', 'usr','bin','env'
print('/'.join(dirs))

low = 'Tronditional alert '
print(low.lower())

name = "Gumby"
names = ['gumby', 'smith', 'jones']
if name.lower() in names:
    print('Found it')

Title = "that's all folks"
print(Title.title())

replaceText = 'This is a test'
print(replaceText.replace('is', 'ees'))

numbers = '1 + 2 + 3 + 4 + 5'
ls = numbers.split('+')
print(ls)

path = '/usr/bin/env'
pls = path.split('/')
print(pls)

str = '    internal whitespace is kept         '
print(str.strip())

str = '*** SPAM * rom * everyone!!!***'
print(str.strip('*!'))

tr = 'this is an incredible test'
table = tr.maketrans('cs', 'kz')
print(tr.translate(table))
