#!/usr/bin/env python
# -*- coding: utf-8 -*-


import types

print(type(123) == int)
print(isinstance(123, int))
print(isinstance([], list))

print(isinstance(abs, types.BuiltinFunctionType))
# print(type(abs) == types.BuiltinFunctionType)     types比较不符合PEP8规范
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance((x for x in range(10)), types.GeneratorType))


def fn():
    pass


print(type(fn))
print(isinstance(fn, types.FunctionType))


class Animal:
    pass


class Pig(Animal):
    pass


print(type(Animal()) == Animal)
print(type(Pig()) == Animal)  # False
print(isinstance(Animal(), Animal))
print(isinstance(Pig(), Animal))
print(isinstance(Animal, object))
print(issubclass(Pig, Animal))
