#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
print('列表拷贝操作：')
list1 = [1, [2, 3]]
list2 = list1
list3 = list1[:]
list4 = copy.copy(list1)
list5 = copy.deepcopy(list1)
print(f'original_list: {list1}')
list1[0] = 111
list1[1][0] = 222
print(f'list1: {list1}, ID: {id(list1)}')
print(f'list2: {list2}, ID: {id(list2)}')
print(f'list3: {list3}, ID: {id(list3)}')
print(f'list4: {list4}, ID: {id(list4)}')
print(f'list5: {list5}, ID: {id(list5)}')

print('\n字典拷贝操作：')
dict1 = {'name': 'Frank', 'hobbies': ['reading', 'running']}
dict2 = dict1
dict3 = dict1.copy()
dict4 = copy.deepcopy(dict1)
print(f'orig_dict: {dict1}')
dict1['name'] = 'Gloria'
dict1['hobbies'][1] = 'gardening'
dict1['hobbies'] = ['walking', 'yoga']
print(f'dict1: {dict1}')
print(f'dict2: {dict2}')
print(f'dict3: {dict3}')
print(f'dict4: {dict4}')
