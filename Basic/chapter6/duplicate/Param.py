__author__ = 'hzliyong'


def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Receivede redundant parameters:', others)
        return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job="king", name='Gumby'))
print(story(name='Sir Robin', job='brave knight'))

params = {'job': 'laguage', 'name': 'python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))

print(power(y=3, x=2))

print(interval(10))

print(interval(1, 5))