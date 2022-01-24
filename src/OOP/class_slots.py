#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType


class People:
    # 限制实例动态添加的方法或属性
    # 对类动态添加的方法或属性不起作用
    # 对子类不起作用
    __slots__ = ('name', 'age', 'set_age')


def set_age(self, age):
    self.age = age


Tom = People()
Tom.name = 'Tom'
# setattr(Tom, 'name', 'Jim')
print(f'Name: {Tom.name}')

# Tom.set_age = MethodType(set_age, Tom)
# Tom.set_age(25)
# setattr(Tom, 'set_age', set_age)
Tom.set_age = set_age
Tom.set_age(Tom, 20)
print(f'Age: {Tom.age}')


@classmethod
def set_num(cls, num):
    cls.num = num
    # print(cls.a)


People.set_num = set_num
People.set_num(12345)
Tom.set_num(888)
print(f'Num: {Tom.num}')
