#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os

data_int = 123
data_str = 'hello'
data_list = ['你好', 'world']
data_tuple = ('hi', [1, 2, 3])
data_dict = {'name': 'Hellen', 'age': 18}


def myfunc(n):
    print(n)


class Person:
    def __init__(self, name):
        self.name = name


pickle_int = pickle.dumps(data_int)
pickle_str = pickle.dumps(data_str)
pickle_list = pickle.dumps(data_list)
pickle_tuple = pickle.dumps(data_tuple)
pickle_dict = pickle.dumps(data_dict)
pickle_func = pickle.dumps(myfunc)
pickle_class = pickle.dumps(Person)

print(f'Load pickle_int: {pickle.loads(pickle_int)}')
print(f'Load pickle_str: {pickle.loads(pickle_str)}')
print(f'Load pickle_list: {pickle.loads(pickle_list)}')
print(f'Load pickle_tuple: {pickle.loads(pickle_tuple)}')
print(f'Load pickle_dict: {pickle.loads(pickle_dict)}')
print(f'Load pickle_func: {pickle.loads(pickle_func)}')  # 只能保存函数名
print(f'Load pickle_class: {pickle.loads(pickle_class)}')  # 只能保存类名


os.chdir('res')
with open('data.pickle', 'wb') as f:
    pickle.dump(data_list, f)

print('\nLoad data from file:')
with open('data.pickle', 'rb') as f:
    print(f'{pickle.load(f)}')
