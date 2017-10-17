# -*- coding: utf-8 -*-
import Queue
import math
q=Queue.Queue(maxsize=10)
for i in range(10):
    q.put(i)
while not q.empty():
    print q.get()

print math.fabs(-1.0)
