#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, active_children, current_process
import os
import time


def run(delay, **kwargs):
    cp = current_process()
    print(f'Process {cp.name} started, Priority: {kwargs["priority"]}')
    time.sleep(delay)
    print(f'{cp.name} PID: {cp.pid}, PPID: {os.getppid()}')


if __name__ == '__main__':
    p1 = Process(target=run, name='P1', args=(2,), kwargs={'priority': 'lower'})
    p2 = Process(target=run, name='P2', args=(1,), kwargs={'priority': 'higher'})
    p1.start()
    p2.start()
    p1.name = 'P11'
    # p1.terminate()
    print(f'Active children processes: {active_children()}')
    p1.join()
    p2.join()
    print(f'{current_process().name} ID: {os.getpid()}')

