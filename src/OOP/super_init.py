#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, skill='run'):
        self.skill = skill

    def show(self):
        print(f'I can {self.skill}.')


# 若子类没有新增属性，则能继承父类所有属性
class Dog(Animal):
    pass


# 当子类有新增属性，若没有调用父类的__init__方法，则不能继承父类属性
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print(f'I am {self.name}.')


# 当子类有新属性时，调用父类的__init__方法后，可继承父类属性
class Horse(Animal):
    def __init__(self, name):
        self.name = name
        print(f'I am {self.name}.')
        super().__init__()
        # 以下等效
        # super(Horse, self).__init__()
        # Animal.__init__(self)


Dog().show()

try:
    Cat('cat1').show()
except Exception as e:
    print(e)

Horse('horse1').show()
