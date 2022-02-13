#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def run():
    rlock.acquire()
    rlock.acquire()
    print(f'{threading.current_thread().name} acquire rlock')
    time.sleep(1)
    rlock.release()
    rlock.release()
    print(f'{threading.current_thread().name} release rlock')


rlock = threading.RLock()

threads = []
t1 = time.time()
for i in range(3):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
t2 = time.time()
print(t2 - t1)
