#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Animal:
    def say(self):
        print('They are animals.')
        return 'animal'


class Horse(Animal):
    color = 'white'

    def say(self):
        print('A horse')
        print(super().say())
        print('Horse is done.')
        return 'horse'


class Donkey(Animal):
    color = 'brown'

    def say(self):
        print('A donkey')
        print(super().say())
        print('Donkey is done.')
        return 'donkey'


class FlyableMixin:
    def fly(self):
        print('I can fly.')


class Mule(Horse, Donkey, FlyableMixin):
    def say(self):
        print(super().say())
        print(f'A {self.color} Mule')


mule1 = Mule()
mule1.say()
mule1.fly()
print(Mule.mro())
# print(isinstance(mule1, Animal))
