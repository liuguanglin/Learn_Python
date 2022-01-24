#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
生成器generator用于创建迭代器
"""


# 生成器的写法类似于标准的函数，但当它们要返回数据时会使用 yield 语句
def print_str(arg_str):
    for i in arg_str:
        yield i


f = print_str('good')
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print('End of generator:', e.value)
        break

print('-' * 20)

# 生成器表达式
g = (i * i for i in range(5))
print(next(g))
print(next(g))
print('-' * 20)
for j in g:
    print(j)
