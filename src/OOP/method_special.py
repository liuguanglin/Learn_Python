#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class People(object):

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        self.name = name

    # 修改print效果
    def __str__(self):
        return f'Name: {self.name}'

    # 修改直接显示的效果
    __repr__ = __str__

    def __call__(self):
        print(f'{self.name} is called.')

    def __setattr__(self, key, value):
        print(f'set {key}={value}')
        object.__setattr__(self, key, value)
        # super().__setattr__(key, value)
        # self.__dict__[key] = value

    # 实例对象访问类属性或实例属性时将调用该方法，类直接访问属性时则不调用
    # def __getattribute__(self, item):
    #     print(f'Access {item}')
    #     return super().__getattribute__(item)
    #     # return object.__getattribute__(self, item)

    # 当被调用的属性不存在时，该方法将被调用
    def __getattr__(self, item):
        return f'No {item}'

    def __delattr__(self, attr):
        print(f'Delete attribute {attr}')
        object.__delattr__(self, attr)

    # 与__setattr()__不同的是，该方法针对字典方式赋值生效
    def __setitem__(self, key, value):
        print('__setitem__')
        self.__dict__[key] = value

    def __getitem__(self, item):
        print(f'Get {item} {self.__dict__.get(item, "xxx")}')
        return self.__dict__.get(item, 'xxx')

    def __delitem__(self, key):
        print(f'Delete item {key}')
        del self.__dict__[key]

    def __del__(self):
        print(f'Destroy {self.name}')


print(dir(People))
Tom = People('Tom')
print(Tom)
Tom()
Tom.age = 18
del Tom.age
print(Tom.age)
Tom['name'] = "Lucy"
print(Tom['name'])
Tom['gender'] = 'F'
del Tom['gender']
print(dir(Tom))
# del Tom
