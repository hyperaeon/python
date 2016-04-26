__author__ = 'hzliyong'

import time
import sys

# for i in range(10):
#     print(i)
#     if i == 5:
#         print("Flushing buffer")
#         sys.stdout.flush()
#     time.sleep(1)

# print("-----------")
for i in range(10):
    print(i)
    if i == 5:
        print("Flushing buffer")
        sys.stdout.flush()