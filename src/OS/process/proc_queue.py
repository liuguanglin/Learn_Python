#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue, current_process


def put_q(q):
    for i in range(5):
        q.put(f'{current_process().name}_' + str(i))


def get_q(q):
    for i in range(5):
        print(f'{current_process().name} get {q.get()}')


if __name__ == '__main__':
    work_queue = Queue()
    put_q(work_queue)

    p_put = Process(target=put_q, name='P_put', args=(work_queue,))
    p_get = Process(target=get_q, name='P_get', args=(work_queue,))
    p_put.start()
    p_get.start()
    p_put.join()
    p_get.join()

    while not work_queue.empty():
        print(f'{current_process().name} get {work_queue.get()}')
