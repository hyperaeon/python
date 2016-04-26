__author__ = 'hzliyong'

def functionName(level):
    if (level < 1):
        raise ("Invalid level!",level)

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except (Networkerror) as e:
    print(e.args)