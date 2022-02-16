#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
与守护线程不同的是，当主进程退出时，守护进程将被立即终止。
"""

from multiprocessing import Process, current_process
import time


def run(delay):
    print(f'{current_process().name} started, will sleep for {delay}s.')
    time.sleep(delay)
    print(f'{current_process().name} exited normally.')


if __name__ == '__main__':
    p1 = Process(target=run, args=(1,))
    p2 = Process(target=run, args=(2,))
    p1.daemon = True
    p1.start()
    p2.start()
    print(f'{current_process().name} exited.')
