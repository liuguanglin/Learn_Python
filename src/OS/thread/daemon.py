#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
当所有前台线程退出后，守护线程将自动退出。
"""

import threading
import time


def task(delay):
    print(f'{threading.current_thread().name} started, will sleep for {delay}s.')
    time.sleep(delay)
    print(f'{threading.current_thread().name} will exit normally.')


task1 = threading.Thread(target=task, args=(2,))
# task1 = threading.Thread(target=task, args=(2,), daemon=True)
task1.daemon = True
task2 = threading.Thread(target=task, args=(1,))
task1.start()
task2.start()
for t in threading.enumerate():
    if t.isDaemon():
        print(t.name, 'is daemon thread.')
print('MainThread stopped.')
