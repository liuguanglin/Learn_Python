#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
文档测试
python my_doctest.py -v

>>> James = Student('James')
>>> James.age = 30
>>> James.age
30
>>> James.gender
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'gender'
"""


class Student:
    def __init__(self, name):
        self.name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


if __name__ == '__main__':
    import doctest

    doctest.testmod()
