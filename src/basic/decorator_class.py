#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Class Decorators
"""


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Good morning.')
        self.func(*args, **kwargs)
        # res = self.func(*args, **kwargs)
        # return res


@Decorator
def hello(name):
    print(f'I am {name}.')


hello('Mary')
print('-' * 20)


class Decorator2:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'{self.arg}')
            func(*args, **kwargs)
        return wrapper


@Decorator2('Hey')
def hi(name):
    print(f'I am {name}.')


hi('Sam')
