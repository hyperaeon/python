__author__ = 'hzliyong'


def story(**kwds):
    return 'Once upon a time, ' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Recived ', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() fro step>0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job='king', name="Gumby"))
print(story(name='Sir ', job='brave'))
print(interval(0))
