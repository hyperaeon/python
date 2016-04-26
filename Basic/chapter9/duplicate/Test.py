__author__ = 'hzliyong'
#-*- encoding: utf8 -*-


def convert_values(values):
    return [value.replace("'", "''").replace(";","").replace("NULL","") for value in values]

# 分号->逗号
def convertd2s(strs):
    strs = strs.replace(';', ",")
    return strs


# resultList = ['1453456796146\tclick\tcheckStock\t\tweb\tWindows XP\t180.127.73.55\tNULL\t_da_ntes_uid=IO1KlczaeAZlzgSdAydrWyAi;\tNULL\tNULL\t2016-01-22\thttp://www.xiupin.com/detail/checkStock?pid=5808236&poId=0&supplierId=4402814&saleMode=1&t=1453111275546\thttp://www.xiupin.com/detail/checkStock?pid=5808236&poId=0&supplierId=4402814&saleMode=1&t=1453111275546\n', '1453456794669\tpage\tunknown\t-1\tapp\tMac OS X\t223.104.5.224\tNULL\tNULL\tNULL\tE4113817E31C5B50202EB95982F20C5A\t2016-01-22\tNULL\thttp://m2.paopao.163.com/m/v2/search?sort=0&key=%E4%BC%91%E9%97%B2&pageIndex=0\n', '1453456794011\tpage\tsearchPage\t\tweb\tWindows 7\t14.23.99.250\tNULL\t_da_ntes_uid=p8lBZ9wzz3rFyckUWpTTxy52;\tNULL\tNULL\t2016-01-22\thttp://www.xiupin.com/search/sycProduct?query=KENZO&frompos=PCHQJXSP3\thttp://www.xiupin.com/search/asycProduct?query=KENZO&frompos=PCHQJXSP3&offset=0&limit=80\n', '1453456793007\tpage\tgoodsPage\t\tweb\tWindows 7\t110.185.140.108\tNULL\t_da_ntes_uid=mBHjELaiElsjrMzPvZeNo3Lb;\tNULL\tNULL\t2016-01-22\thttp://www.tyeee.com/bh/10000.html\thttp://www.xiupin.com/saleDetail?saleType=1&supplierId=9151&pid=106335\n', '1453456790804\tpage\tsearchPage\t\tweb\tWindows 7\t14.23.99.250\tNULL\t_da_ntes_uid=p8lBZ9wzz3rFyckUWpTTxy52;\tNULL\tNULL\t2016-01-22\thttp://www.xiupin.com/?smtid=442193209z16sozcqumz1pdz0z\thttp://www.xiupin.com/search/sycProduct?query=KENZO&frompos=PCHQJXSP3\n', '1453456786245\tpage\tunknown\t-1\tapp\tMac OS X\t61.148.242.95\tNULL\tNULL\tNULL\t54EE3CCBC19986A02C8C421202568482\t2016-01-22\tNULL\thttp://m2.paopao.163.com/m/v2/search?sort=0&key=%E5%8F%8C%E8%82%A9%E5%8C%85&pageIndex=0\n', '1453456785821\tclick\tcheckStock\t\tweb\tWindows 7\t221.207.10.179\tNULL\t_da_ntes_uid=nglsnMS46ejs8Lw9A16OJKCS;\tNULL\tNULL\t2016-01-22\thttp://www.xiupin.com/detail/checkStock?pid=86839&poId=0&supplierId=7106&saleMode=1&t=1452160664526\thttp://www.xiupin.com/detail/checkStock?pid=86839&poId=0&supplierId=7106&saleMode=1&t=1452160664526\n', '1453456785077\tpage\tgoodsPage\t\tweb\tWindows XP\t183.184.123.140\tNULL\t_da_ntes_uid=UKE8hvO0zV6CWODCdafjMg3h;\tNULL\tNULL\t2016-01-22\t\thttp://www.xiupin.com/saleDetail?saleType=1&supplierId=7106&pid=86839\n', '1453456783037\tpage\thomePage\t12823149\tweb\tWindows 8\t1.86.18.35\tNULL\t_da_ntes_uid=d4LR0WbGWbKVB4EYGHt022sy;\tNULL\tNULL\t2016-01-22\t\thttp://www.xiupin.com/?__da_fvxKel_f9vnCt\n']
resultList = ['1453456785821\tclick\tcheckStock\t\tweb\tWindows 7\t221.207.10.179\tNULL\t_da_ntes_uid=nglsnMS46ejs8Lw9A16OJKCS;\tNULL\tNULL\t2016-01-22\thttp://www.xiupin.com/detail/checkStock?pid=86839&poId=0&supplierId=7106&saleMode=1&t=1452160664526\thttp://www.xiupin.com/detail/checkStock?pid=86839&poId=0&supplierId=7106&saleMode=1&t=1452160664526\n', '1453456785077\tpage\tgoodsPage\t\tweb\tWindows XP\t183.184.123.140\tNULL\t_da_ntes_uid=UKE8hvO0zV6CWODCdafjMg3h;\tNULL\tNULL\t2016-01-22\t\thttp://www.xiupin.com/saleDetail?saleType=1&supplierId=7106&pid=86839\n', '1453456783037\tpage\thomePage\t12823149\tweb\tWindows 8\t1.86.18.35\tNULL\t_da_ntes_uid=d4LR0WbGWbKVB4EYGHt022sy;\tNULL\tNULL\t2016-01-22\t\thttp://www.xiupin.com/?__da_fvxKel_f9vnCt\n']
count = 0

columns = ['TIME','ACTION','TYPE','ACCOUNTID','CLIENTTYPE',
               'DEVICEOS','IP','APPVESION',
               'COOKIE','ORDERID','DEVICEID','REFERER','REQUESTURL',
               'DAY']

for seg in resultList:
    # print("resultList长度：%s" % len(resultList))

    segList = seg.strip().split("\t")
    print("segList:%s " % segList )
    if len(segList) < 14:
        continue
    count += 1

    time = segList[0]
    action = segList[1]
    type = segList[2]
    accountid = segList[3]
    clienttype = segList[4]
    deviceos = segList[5]
    ip = segList[6]
    appvesion = segList[7]
    cookie = segList[8]
    # if not cookie or cookie != '':
    #     cookie.replace(";","")
    orderid = segList[9]
    deviceid = segList[10]
    day = segList[11]
    referer = segList[12]
    requesturl = segList[13]

    insertList = []
    insertList.append(str(time))
    insertList.append(str(action))
    insertList.append(str(type))
    insertList.append(str(accountid))
    insertList.append(str(clienttype))
    insertList.append(str(deviceos))
    insertList.append(str(ip))
    insertList.append(str(appvesion))
    insertList.append(str(cookie))
    insertList.append(str(orderid))
    insertList.append(str(deviceid))
    insertList.append(str(referer))
    insertList.append(str(requesturl))

    joinColumns = ','.join(convert_values(columns))
    print("join columns: " + joinColumns)
    print("len joinColumns %s " % len(joinColumns))

    insertValues = convert_values(insertList)
    print("insertValues %s " % insertValues)
    convertd = convertd2s("','".join(insertValues))
    print("convertd2s:  " + convertd)
    print("len convertd : " + len(convertd))
    # ','.join(oracle_util.convert_values(columns)),convertd2s("','".join(oracle_util.convert_values(insertList)))
print(count)


