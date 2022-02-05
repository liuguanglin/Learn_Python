#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def insertion(alist):
    for i in range(1, len(alist)):
        curr_val = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > curr_val:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = curr_val


def insert_rev(alist):
    for i in range(len(alist) - 2, -1, -1):
        curr_val = alist[i]
        j = i + 1
        while j < len(alist) and alist[j] < curr_val:
            alist[j - 1] = alist[j]
            j = j + 1
        alist[j - 1] = curr_val


lst = [random.randint(1, 100) for x in range(10)]

print('Before sorting:\n', lst)
insertion(lst)
print('After sorting:\n', lst)
