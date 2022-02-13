#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def purchase():
    global NUM
    cond.acquire()
    while True:
        if NUM < 5:
            NUM = NUM + 1
            print(f'已采购一件，库存{NUM}件。')
        else:
            print('库存充足，停止采购。')
            cond.notify(1)
            cond.wait()
        time.sleep(0.1)


def consumption():
    global NUM
    while True:
        cond.acquire()
        if NUM > 0:
            NUM = NUM - 1
            print(f'{threading.current_thread().name}消耗了一件，还剩{NUM}件。')
        else:
            print(f'{threading.current_thread().name}提示库存不足，需采购。')
            # 若有多个消费者，可能会连续多次提示库存不足。
            cond.notify_all()
            cond.wait()
        cond.release()
        time.sleep(0.1)


NUM = 0
cond = threading.Condition()

pur = threading.Thread(target=purchase)
cons = threading.Thread(target=consumption, name='张三')
cons2 = threading.Thread(target=consumption, name='李小四')
pur.start()
cons.start()
cons2.start()
