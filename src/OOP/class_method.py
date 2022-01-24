#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog:
    name = 'Tod'

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'I am {self.name}')

    @classmethod
    def eat(cls, food):
        print(f'{cls.name} is eating {food}.')

    #  在静态方法中无法调用任何类属性和方法
    @staticmethod
    def say(speak):
        print(speak)

    # 实例方法只能由实例对象调用
    def run(self):
        print(f'{self.name} is running.')


Dog.eat('meat')
Dog.say('Hello')
dog1 = Dog('Bear', 'white')
dog1.eat('carrot')
dog1.say('汪汪汪')
dog1.run()
