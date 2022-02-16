#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, BoundedSemaphore, current_process
import time


def run(s):
    s.acquire()
    print(f'{current_process().name} is running at {time.ctime()}.')
    time.sleep(1)
    s.release()


if __name__ == '__main__':
    semaphore = BoundedSemaphore(2)
    for i in range(6):
        Process(target=run, args=(semaphore,)).start()
