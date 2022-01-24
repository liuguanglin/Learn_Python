#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
可以通过for循环来遍历某个对象，这种遍历被称为迭代（Iteration）。
可以直接作用于for循环的对象统称为可迭代对象（Iterable）。
可以被next()函数调用并不断返回下一个值的对象称为迭代器（Iterator）。

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
"""

from collections.abc import Iterable, Iterator

print('Str Iterable? ', isinstance('hello', Iterable))
print('Str Iterator?', isinstance('hello', Iterator))
print('List Iterable?', isinstance([], Iterable))
print('List Iterator?', isinstance([], Iterator))
print('range() Iterable?', isinstance(range(5), Iterable))
print('range() Iterator?', isinstance(range(5), Iterator))
print('Num Iterable?', isinstance(123, Iterable))
print(isinstance(iter([]), Iterator))
