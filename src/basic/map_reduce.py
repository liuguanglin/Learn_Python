#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

"""
map(function, iterable, ...)
返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。

functools.reduce(function, iterable[, initializer])
将function从左至右积累地应用到iterable的条目，以便将该可迭代对象缩减为单一的值。
作用相当于：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

filter(function, iterable)
将function作用于iterable中的每个元素，将返回真的元素构建一个新的迭代器。
"""


def func(n):
    return n * 10


print(list(map(func, [1, 2, 3])))
print(list(map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4]))


print(list(filter(lambda x: x % 2, range(10))))
