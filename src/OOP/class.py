#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog:
    name = '旺财'

    def __init__(self, name, color):
        self.name = name
        self.__color = color

    def get_color(self):
        print(f'{self.name} is {self.__color}')

    def set_color(self, color):
        self.__color = color


def run(self):
    print(f'{self.name} is running.')


dog1 = Dog('xiaohei', 'black')
# 私有属性不能被公开访问，也不能被子类访问
# print(dog1.__color)
assert not hasattr(dog1, '__color')
# 可从__dict__中查看私有属性的真实名称
print(dog1._Dog__color)
dog1.get_color()
dog1.set_color('green')
dog1.get_color()

# 不能从外部直接修改私有变量
# dog1._Dog__color = 'yellow'
dog1.__color = 'yellow'
print('New attribute: ', dog1.__color)
dog1.get_color()
del dog1.name
print(dog1.name)  # 实例属性可将类属性屏蔽
print(Dog.name)
# print(Dog._age)

# 可动态添加类和实例的属性、方法
Dog.name = 'Droppy'
Dog.run = run
dog1.run()
dog1.age = 5
print(f'{dog1.name} is {dog1.age} years old.')
print('Attributes and methods of instance dog1:\n', dog1.__dir__())
