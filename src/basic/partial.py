#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial

"""
functools.partial的作用是，给一个函数设置默认参数，再返回一个新的函数。
"""

int2 = partial(int, base=2)
print(int2('1000'))

max2 = partial(max, 10)
print(max2(5, 6, 7))

func = partial(lambda x, y: x + y, y=100)
print(func(5))
