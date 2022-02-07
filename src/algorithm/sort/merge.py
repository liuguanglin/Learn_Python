#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
merge_sort(lst)
print('After sorting:')
print(lst)
