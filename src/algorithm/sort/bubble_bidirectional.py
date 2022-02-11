#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def bidirectional_bubble(alist):
    size = len(alist)
    left = 0
    right = size - 1
    while left < right:
        exchange = False
        for i in range(left, right):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchange = True
        right -= 1
        if not exchange:
            break
        for i in range(right, left, -1):
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
        left += 1


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
bidirectional_bubble(lst)
print('After sorting:')
print(lst)
