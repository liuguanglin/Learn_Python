#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@property装饰器能把实例方法以属性的形式使用，被装饰的方法只能有一个参数self。
同时产生@属性名.setter、@属性名.getter、@属性名.deleter装饰器，用于对属性进行修改、取值和删除。
"""


class People:
    @property
    def info(self):
        print(self._name, self._age)

    @info.setter
    def name(self, name):
        self._name = name

    @info.setter
    def age(self, age):
        self._age = age

    @info.deleter
    def del_age(self):
        print('delete age')
        del self._age


p1 = People()
p1.name = 'Tom'
p1.age = 20
p1.info
del p1.del_age


# 属性名不要和实例变量重名，否则将造成无限递归，最终导致栈溢出报错RecursionError。
class People:
    @property
    def name(self):
        return self.name


p2 = People()
try:
    p2.name()
except RecursionError as re:
    print(re)
