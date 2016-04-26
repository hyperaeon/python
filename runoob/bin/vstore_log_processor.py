#!/usr/bin/python

import sys
import subprocess
import pydoop

__author__ = 'hzliyong'


def run_shell_command(command, try_run=False):
    print("----Execute-----")
    print('%s' % command)
    if not try_run:
        print('-----Output------')
        sys.stdout.flush()
        return subprocess.call(command, shell=True)
    else:
        return 'This is try run'


def start_task(day, try_run=False):
    jar_path = 'shangou-etl-jar-with-dependencies.jar'
    output_compressor = '-D mapred.output.compress=true -D mapred.output.compression.codec=com.hadoop.compression.lzo.LzopCodec'

    main_class = 'com.netease.da.shangou.etl.LogProcessor'
    input_path = '/datastream/user/xiupin/log/online/%s' % day
    output_path = '%s/%s' %('/home/appops/apache-hive1.2.1', day)
