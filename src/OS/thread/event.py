#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def order():
    print('点完菜，等待上菜……')
    while not event.is_set():
        time.sleep(0.6)
        print('菜好了没？') if not event.is_set() else print('真的来了')
    # event.wait()
    print('开吃！')


def serve():
    time.sleep(2)
    event.set()
    print('菜来了……')


event = threading.Event()
# event.clear()
customer = threading.Thread(target=order)
waiter = threading.Thread(target=serve)
customer.start()
waiter.start()
event.wait()
