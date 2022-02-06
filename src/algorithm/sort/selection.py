#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def select_min(alist):
    for i in range(len(alist) - 1):
        min_loc = i
        for j in range(i + 1, len(alist)):
        # for j in range(len(alist) - 1, i, -1):
            if alist[j] < alist[min_loc]:
                min_loc = j
        alist[min_loc], alist[i] = alist[i], alist[min_loc]


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
select_min(lst)
print('After sorting:')
print(lst)
