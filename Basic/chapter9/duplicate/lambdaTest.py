__author__ = 'hzliyong'

bar = lambda: "hello"
print(bar())

batch_values = [None, 3, None]
batch_values = filter(lambda x: x != None, batch_values)
print(list(batch_values))


def listFunc(*args):
    for a in args:
        print(a)


ls = [2, 3, 4]
listFunc(ls)

tu = (1, 3, 3)
listFunc(tu)

dic = {"a": 1, "b": 2}
listFunc(dic)


def add(x, y):
    return x + y


add2 = lambda x, y: x + y
print(add(1, 3))
print(add2(1, 2))


def sum(x, y=10):
    return x + y


mylist = []
mylist.append('')
mylist.append('')
print(mylist)

cookie = ';'
if not cookie or cookie != '':
    cookie = cookie.replace(";", '')
print("cookie: ", cookie)

result = ''''1453528671073\tpage\thomePage\t\tweb\tWindows XP\t111.50.0.246\tNULL\t_da_ntes_uid=PlxprvZJK50DrrdtfuovZhXO;\tNULL\tNULL\t2016-01-23\thttp://paopao.163.com/\thttp://www.xiupin.com/\n', '''
lst = result.strip().split("\t")
print(len(lst))
for a in lst:
    print("a: ", str(a))
