#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import queue
import time
import random


class MyThread(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        get_q(self.q)


def get_q(q):
    while not my_queue.empty():
        print(f'{threading.current_thread().name}-->{q.get()}')
        time.sleep(random.random())


my_queue = queue.Queue(10)
# my_queue = queue.LifoQueue(10)
for i in range(10):
    my_queue.put(i)

for i in range(3):
    MyThread(my_queue).start()

for mythread in threading.enumerate():
    if mythread._name != 'MainThread':
        mythread.join()
print('MainThread exited.')
