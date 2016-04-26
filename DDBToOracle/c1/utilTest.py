# _*_encoding=utf-8_*_
__author__ = 'hzliyong'

day = '2016-01-25'

columns = ['TIME', 'ACTION', 'TYPE', 'ACCOUNTID', 'CLIENTTYPE', 'DEVICETYPE',
           'DEVICEOS', 'IP', 'LONGITUDE', 'LATITUDE', 'DEVICEMODEL', 'DEVICERESOLUTION',
           'DEVICEPLATFORM', 'DEVICENETWORK', 'DEVICEOSVERSION', 'DEVICEUDID', 'APPCHANNEL',
           'APPVESION', 'BROWSER', 'COOKIE', 'REFER', 'BRANDID', 'BRANDNAME', 'POID', 'STATUS',
           'ORDERID', 'SKULIST', 'URL', 'SKUID', 'CHANGEFROM', 'CHANGETO', 'PID', 'AREACODE', 'PROVINCECODE',
           'GOODSNO', 'ROBOT', 'FIRSTCATEGORYID', 'SKUPRICECNTLIST', 'FROMPOS', 'TYPENAME', 'SEARCHCHANNEL',
           'SEARCHTYPE', 'MINSALEPRICE', 'MAXSALEPRICE', 'SUCCESS', 'TOTALHIT', 'IDS', 'BRANDIDS', 'CATEGORY',
           'KEYWORD', 'BRANDBUY', 'GLOBALBUY', 'DEVICEID', 'DAY', 'REFERER', 'REQUESTURL']

hql = ''' select time,action,type,accountid,clienttype,devicetype,deviceos,ip,longitude,latitude,devicemodel,
                    deviceresolution,deviceplatform,devicenetwork,deviceosversion,deviceudid,
                    appchannel,appvesion,browser,cookie,refer,brandid,brandname,poid,status,orderid,
                    skulist,url,skuid,changefrom,changeto,pid,areacode,provincecode,goodsno,robot,firstcategoryid,
                    skupricecntlist,frompos,typename,searchchannel,searchtype,minsaleprice,maxsaleprice,success,totalhit,ids,
                    brandids,category,keyword,brandbuy,globalbuy,deviceid,day,referer,requesturl from vstore_log where day>='{0}'
            '''.format(day)


def exec_cmd(cmd, output=False):
    hive_cmd = '{} -e "{}" '.format('a', cmd)
    if output:
        return "output"
    else:
        return "none"


def query_hql(hql, jobname=None, **conf_args):
    cmd_list = []
    for name, value in conf_args.items():
        cmd_list.append('set {}={};'.format(name, value))
    cmd_list.append(hql)
    return exec_cmd(" ".join(cmd_list), output=True)


def export_hql_to_db(hql, table, columns, conn, batch_size=1024, jobname=(None, 1), convert_func=None, *args):
    values = []
    for line in query_hql(hql):
        if convert_func:
            line = convert_func(line, jobname=jobname, *args)
            print("line %s" % line)
        item = line.strip().split('\t')
        print("item %s" % item)
        if len(item) != len(columns):
            raise Exception(), "columns size not match expect {} get {}".format(len(columns), len(item))
        values.append(item)
        if len(values) >= batch_size:
            print("values >= batch_size")
    if values:
        print("values")


# export_hql_to_db('use %s;' % hql, 'shangou_da', 'VSTORE_LOG', columns, [0], -1)

line = '''1453607982349\tpage    homePage web  \t \t  Unknown Unknown 123.125.71.116  NULL    NULL  NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    Robot/Spider    _da_ntes_uid=5CqiCFVQaA4DCUarFSXBgnFt;       NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL           NULL    NULL    NULL    NULL    NULL    11      NULL    1           NULL    NULL��ҳ    NULL    NULL    NULL    NULL    NULL    NULL                NULL    NULL    NULL    NULL    NULL    NULL    NULL                 2016-01-24              http://www.wenyou.xiupin.com/'''
print(line.strip().replace('\t','@@')).replace(";","")
item = line.strip().replace('\t','@@').split('@@')
print(item)
print(len(item))
print(len(columns))
values=[]
values.append(item)
print(values)
if len(item) != len(columns):
    print("not equals")


print(type(-1) == type(()))