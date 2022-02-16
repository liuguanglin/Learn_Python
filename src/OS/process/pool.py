#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool, active_children


def run(n):
    print(f'P{n} started.')
    return n * 10


def call_back(arg):
    print(f'Call back: {arg}')


if __name__ == '__main__':
    pool = Pool()
    for i in range(10):
        pool.apply_async(run, args=(i,), callback=call_back)
    pool.close()
    print(f'Active child processes: {len(active_children())}')
    pool.join()
