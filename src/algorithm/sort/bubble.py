# -*- coding: utf-8 -*-

import random


def bubble(alist):
    for i in range(len(alist) - 1):
        exchange = False
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        if not exchange:
            break


lst = [random.randint(1, 100) for i in range(10)]
print('Before sorting:')
print(lst)
bubble(lst)
print('After sorting:')
print(lst)
