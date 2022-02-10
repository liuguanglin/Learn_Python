#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def shell_sort(alist):
    size = len(alist)
    gap = size // 2
    while gap > 0:
        for start in range(gap):
            for i in range(start + gap, size, gap):
                tmp = alist[i]
                j = i - gap
                while j >= start and alist[j] > tmp:
                    alist[j + gap] = alist[j]
                    j = j - gap
                alist[j + gap] = tmp
        gap = gap // 2


def shell_sort2(alist):
    size = len(alist)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            tmp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > tmp:
                alist[j] = alist[j - gap]
                j = j - gap
            alist[j] = tmp
        gap = gap // 2


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
shell_sort(lst)
print('After sorting:')
print(lst)
