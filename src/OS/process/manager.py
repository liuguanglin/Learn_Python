#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Manager, Process, Lock


def run(l, lock):
    # with lock:
    lock.acquire()
    for _ in range(100):
        l[0] -= 1
    lock.release()


if __name__ == '__main__':
    mutex_lock = Lock()
    # 以下可使用m = Manager()
    with Manager() as m:
        lst = m.list([200])
        p_list = []
        for i in range(2):
            p = Process(target=run, args=(lst, mutex_lock))
            p_list.append(p)
            p.start()
        # 使用Manager()时，子进程必须阻塞主进程
        for p in p_list:
            p.join()
        print(lst)
