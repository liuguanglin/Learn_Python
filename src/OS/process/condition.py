#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Condition, Manager, current_process
import time


def purchase(c, stocks):
    c.acquire()
    while True:
        if stocks['num'] < 5:
            stocks['num'] = stocks['num'] + 1
            print(f"已采购一件，库存{stocks['num']}件。")
        else:
            print('库存充足，停止采购。')
            c.notify()
            c.wait()
        time.sleep(0.1)


def consumption(c, stocks):
    while True:
        c.acquire()
        if stocks['num'] > 0:
            stocks['num'] = stocks['num'] - 1
            print(f"{current_process().name}消耗了一件，还剩{stocks['num']}件。")
        else:
            print(f'{current_process().name}提示库存不足，需采购。')
            c.notify_all()
            c.wait()
        c.release()
        time.sleep(0.1)


if __name__ == '__main__':
    m = Manager()
    goods = m.dict({'num': 0})
    cond = Condition()

    pur = Process(target=purchase, args=(cond, goods))
    cons = Process(target=consumption, name='张三', args=(cond, goods))
    pur.start()
    cons.start()
    pur.join()
    cons.join()
