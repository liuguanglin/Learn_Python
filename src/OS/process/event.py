#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Event
import time


def order(event):
    print('点完菜，等待上菜……')
    while not event.is_set():
        time.sleep(0.6)
        print('菜好了没？') if not event.is_set() else print('真的来了')
    # event.wait()
    print('开吃！')


def serve(event):
    time.sleep(2)
    event.set()
    print('\033[1;32m菜来了……\033[0m')


if __name__ == '__main__':
    e = Event()
    # e.clear()
    customer = Process(target=order, args=(e,))
    waiter = Process(target=serve, args=(e,))
    customer.start()
    waiter.start()
    e.wait()
