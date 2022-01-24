#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
List Comprehensions 列表推导式
对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。
"""

squares = [x * x for x in range(1, 5)]
print(squares)

even_l = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_l)

num_l = [x if x % 2 == 1 else -x for x in range(1, 11)]
print(num_l)

combs = [x + y for x in 'ABC' for y in '12']
print(combs)

d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d1 = [k + '=' + v for k, v in d.items()]
print(d1)
