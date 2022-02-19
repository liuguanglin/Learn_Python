#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool


def amplify(n):
    return n * 10


if __name__ == '__main__':
    pool = Pool()
    lst_init = [i for i in range(10)]
    lst_map = pool.map(amplify, lst_init)
    # pool.close()
    # pool.join()
    print(lst_init)
    print(lst_map)
