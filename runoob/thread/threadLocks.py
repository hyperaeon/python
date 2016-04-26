#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'hzliyong'

import threading
import time

threadLock = threading.Lock()
threads = []


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name;
        self.counter = counter

    def run(self):
        print("Starting... " + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s " % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, "Thread-1", 2)
thread2 = myThread(2, "Thread-2", 1)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for r in threads:
    r.join()

print("Exiting Main Thread")
