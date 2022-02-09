#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def sort_entry(alist):
    quick_sort(alist, 0, len(alist) - 1)


def quick_sort(alist, first, last):
    if first < last:
        split_loc = partition(alist, first, last)
        quick_sort(alist, first, split_loc - 1)
        quick_sort(alist, split_loc + 1, last)


def partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last
    while left <= right:
        while left <= right and alist[left] <= pivot:
            left = left + 1
        while left <= right and alist[right] >= pivot:
            right = right - 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
            left = left + 1
            right = right - 1
    alist[right], alist[first] = alist[first], alist[right]
    return right


lst = random.sample(range(100), 10)
print('Before sorting:')
print(lst)
sort_entry(lst)
print('After sorting:')
print(lst)
