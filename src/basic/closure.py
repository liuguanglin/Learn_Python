#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Closure闭包：
在一个函数内部定义了另一个函数，并且这个内部函数对外部函数作用域的变量进行引用，该内部函数被称为闭包。
"""


def outer(text):
    def inner():
        print(f'Hello, {text}.')

    return inner


myfunc = outer('dog')
myfunc()
print(myfunc.__name__)
print(myfunc.__closure__[0].cell_contents)


# 闭包的延迟绑定，闭包中用到的变量值是在函数被调用时才获取的。
def multipliers():
    return [lambda x: x * i for i in range(5)]


print([m(10) for m in multipliers()])


# def multipliers():
#     mul_lst = []
#     for i in range(5):
#         def multiplier(x):
#             return i * x
#
#         mul_lst.append(multiplier)
#     return mul_lst
#
#
# for m in multipliers():
#     print(m(10))


def multipliers():
    return [lambda x, i=i: x * i for i in range(5)]


print([m(10) for m in multipliers()])


def multipliers():
    mul_lst = []
    for i in range(5):
        def multiplier(x, i=i):
            return i * x

        mul_lst.append(multiplier)
    return mul_lst


for m in multipliers():
    print(m(10))
