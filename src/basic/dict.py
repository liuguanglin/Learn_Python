#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从Python 3.6开始，字典按照插入的顺序迭代
"""
import operator
from collections import defaultdict

# 创建字典的几种方法
person = {'name': 'Dennis', 'age': 20, 'sex': 'M'}
ext_info = dict(addr='xxxxx', phone='123456')

# 更新字典
person.update(ext_info)
person['hobbies'] = ['sewing', 'kayaking', 'archery']
person['phone'] = '666666'
print(person.setdefault('score', 80))

# 浅拷贝
person_copy = person.copy()

print(person)
print('name' in person, '\n')
print('Email:', person.get('Email', 'Null'), '\n')
print('person.keys()==>', person.keys(), '\n')
print('person.values()==>', list(person.values()), '\n')
print('person.items():', person.items())
del person['score']
print('-' * 20)

for x, y in enumerate(person, start=100):
    print('{}, {}'.format(x, y))

print(sorted(ext_info.items(), key=lambda s: s[1], reverse=True))
print(sorted(ext_info.items(), key=operator.itemgetter(1), reverse=True))

person.clear()
del person

# 创建字典的其他方法
dict_fromkeys = dict().fromkeys(list(range(5)), 'value')
print('fromkeys()==>', dict_fromkeys, '\n')

# mydict = defaultdict(lambda: 0)
dict_default = defaultdict(int)
print('defaultdict()==>', dict_default[1], '\n')

lst1 = ['k1', 'k2', 'k3']
lst2 = [1, 2]
print(dict(list(zip(lst1, lst2))))
