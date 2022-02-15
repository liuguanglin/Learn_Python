#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def bidirectional_selection(alist):
    left = 0
    right = len(alist) - 1
    while left < right:
        for i in range(len(alist) // 2):
            min_loc = left
            max_loc = right
            for j in range(i, right + 1):
                if alist[j] < alist[min_loc]:
                    min_loc = j
                if alist[j] > alist[max_loc]:
                    max_loc = j
            # 若左右两端分别为最大、最小的元素，可直接交换
            if alist[left] == alist[max_loc]:
                alist[left], alist[min_loc] = alist[min_loc], alist[left]
                alist[right], alist[min_loc] = alist[min_loc], alist[right]
            else:
                alist[left], alist[min_loc] = alist[min_loc], alist[left]
                alist[right], alist[max_loc] = alist[max_loc], alist[right]
            left += 1
            right -= 1


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
bidirectional_selection(lst)
print('After sorting:')
print(lst)
