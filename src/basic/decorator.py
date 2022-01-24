#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

"""
decorator装饰器：
返回值为另一个函数的函数，通常使用 @wrapper 语法形式来进行函数变换。
"""


def decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print('Good morning.')
        func(*args)
        # return func(*args, **kwargs)

    return wrapper


@decorator
def hello(name):
    print(f'I am {name}.')


# hello = decorator(hello)
hello('Jack')
print('Function name: ', hello.__name__)
print('-' * 20)


# 带参数的装饰器
def info(value, *args_dec, **kwargs_dec):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """doc of wrapper"""
            print(value)
            return func(*args, **kwargs)
        return wrapper
    return dec


@info('hello')
def hey(name):
    print(f'I am {name}.')


# hey=info('Hi')(hey)
hey('Tom')
print('function name:', hey.__name__)
