#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 100


def hi(self):
    print('Hi, human.')


# 动态创建类
MyClass = type('MyClass1', (object, ), {'a': a, 'hi': hi})
MyClass().hi()
print(dir(MyClass))


class MyMeta(type):

    def hello(cls):
        print('hello, world.')

    def __new__(cls, name, bases, attrs):
        print(name, bases, attrs)
        attrs['hello'] = cls.hello
        return super().__new__(cls, name, bases, attrs)
        # return type(name, bases, attrs)


class A(metaclass=MyMeta):
    x = 100


print('-' * 20)
print(A.__dict__)
print(A.__class__)


def MyMeta2(name, bases, attrs):
    print(name, bases, attrs)
    attrs['hi'] = hi
    return type(name, bases, attrs)


class B(metaclass=MyMeta2):
    pass


print('-' * 20)
print(B.__dict__)
