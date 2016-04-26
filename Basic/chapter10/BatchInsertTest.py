__author__ = 'hzliyong'


def batch(alist) :
    batchcnt = 2
    lens = len(alist)
    if lens < batchcnt:
        print("less than batchcnt")

    idxcnt = 0
    tmplist = []
    for item in alist:
        idxcnt = idxcnt + 1
        if (idxcnt % batchcnt == 0):
            tmplist.append(item)
            batchsql = ';\n'.join(tmplist)
            print('sql: \n%s' % batchsql)
            tmplist = []
            print('ok!!')
        else :
            tmplist.append(item)

    tmplist = []
    lenmod = lens % batchcnt
    tmplist = alist[(lens-lenmod):lens]
    batchsql = ';\n'.join(tmplist)
    print('sql: \n%s' % batchsql)
    tmplist = []
    print('ok!!!')

alist = ['aaa','bbb','ccc']
batch(alist)