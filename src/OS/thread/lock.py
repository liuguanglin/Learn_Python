#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

NUM = 0
lock = threading.Lock()


def count():
    global NUM
    lock.acquire()
    for _ in range(1_000_000):
        NUM += 1
    for _ in range(1_000_000):
        NUM -= 1
    lock.release()
    print(f'{threading.current_thread().name} result: {NUM}')


for i in range(5):
    threading.Thread(target=count).start()
