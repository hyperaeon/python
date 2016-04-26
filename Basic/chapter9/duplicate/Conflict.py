__author__ = 'hzliyong'


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


def queens2(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens2(num, state + (pos,)):
                    yield (pos,) + result

for solution in queens2(8):
    print(solution)


print(list(queens(4, (1, 3, 0))))

state = (0, 0)
print(len(state))
