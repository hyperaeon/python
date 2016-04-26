__author__ = 'hzliyong'


def jar(*args):
    print('exec jar ')


def unknow(*args):
    pass

COMMANDS = {"jar": jar}
COMMAND = "jar2"
(COMMANDS.get(COMMAND, unknow))("ABC")