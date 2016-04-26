__author__ = 'hzliyong'
import time

def procedure():
    time.sleep(0.1)

t0 = time.clock()
procedure()
print(time.clock() - t0, "Seconds process time")

t0 = time.time()
procedure()
print(time.time() - t0, "seconds wall time")


ticks = time.time()
print("Current Time: ", ticks)

localtime = time.localtime(ticks)
print("Local current time", localtime)

localasctime = time.asctime(localtime)
print("local asc time", localasctime)