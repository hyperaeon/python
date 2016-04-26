# -*- coding: utf-8 -*-

__author__ = 'hzliyong'


def ad_analyze(day):
    '''曝光统计'''
    exp_all = '''select day,'0',channel,exposure,webpage,position,count(position) exp from vstore_log where exposure is not null and position is not null and day='{0}' group by day,position,webpage,exposure,channel;'''.format(
        day)
    exp_pc = '''select day,'1',channel,exposure,webpage,position,count(position) exp from vstore_log where exposure is not null and position is not null and day='{0}' and clientType='web' group by day,position,webpage,exposure,channel;'''.format(
        day)
    exp_mobile = '''select day,'2',channel,exposure,webpage,position,count(position) exp from vstore_log where exposure is not null and position is not null and day='{0}' and clientType<>'web' group by day,position,webpage,exposure,channel;'''.format(
        day)
    '''广告点击统计'''
    rel_all = '''select day,'0',channel,release,webpage,position,count(position) rel from tb_test where (release is not null ) and position is not null and day='{0}' group by day,position,webpage,release,channel;'''.format(
        day)
    rel_pc = '''select day,'1',channel,release,webpage,position,count(position) rel from tb_test where (release is not null ) and position is not null and day='{0}' and clientType='web' group by day,position,webpage,release,channel;'''.format(
        day)
    rel_mobile = '''select day,'2',channel,release,webpage,position,count(position) rel from tb_test where (release is not null ) and position is not null and day='{0}' and clientType<>'web' group by day,position,webpage,release,channel;'''.format(
        day)
    hqls = [exp_all, exp_pc, exp_mobile, rel_all, rel_pc, rel_mobile]
    columns = ['LOG_DAY', 'TERMINAL_TYPE', 'CHANNEL', 'EXPOSURE', 'WEBPAGE', 'POSITION', 'EXPOS']
    count = 0
    for hql in hqls:
        count += 1
        if count > 3:
            columns[6] = 'CLICK'
        print(columns)


ad_analyze('2016-02-24')


def run_all(day):
    print("run_all")


def unknown(day):
    print("unknown")


def main(args):
    COMMANDS = {'ad_analyze': ad_analyze,
                'all': run_all,
                'unknown': unknown}
    job, day = args[0], None
    if len(args) >= 2:
        day = args[1]
    (COMMANDS.get(job, unknown))(day)

main('abc')