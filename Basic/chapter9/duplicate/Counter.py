__author__ = 'hzliyong'


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__()

c1 = CounterList(range(10))
print(c1)