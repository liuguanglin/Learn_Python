#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
匿名函数只能有一个表达式，且必须要有返回值。
"""

print((lambda x: 'odd' if x % 2 else 'even')(50))


# lambda 函数可以引用包含作用域中的变量
def increment(n):
    return lambda x: x + n


f = increment(50)
print(f(1))

# 可把匿名函作为参数传递
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
