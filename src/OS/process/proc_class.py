#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, active_children, current_process
import os
import time


class MyProc(Process):
    def __init__(self, name, delay, kwargs):
        super().__init__()
        self.name = name
        self.delay = delay
        self.dict = kwargs

    def run(self):
        print(f'Process {self.name} started, Priority: {self.dict["priority"]}')
        time.sleep(self.delay)
        print(f'{self.name} PID: {current_process().pid}, PPID: {os.getppid()}')


if __name__ == '__main__':
    p1 = MyProc('P1', 2, kwargs={'priority': 'lower'})
    p2 = MyProc('P2', 1, kwargs={'priority': 'higher'})
    p1.start()
    p2.start()
    p1.name = 'P11'
    print(f'Active children processes: {active_children()}')
    p1.join()
    p2.join()
    print(f'{current_process().name} ID: {os.getpid()}')
