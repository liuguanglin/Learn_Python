#!/usr/bin/env python
# -*- coding: utf-8 -*-


print('{0}-{1}-{0}'.format('Good', 'morning'))
print('{}-{}'.format('你', '好'))
print('{name}:{age}'.format(name='Tom', age=18))

x, y = 100, 200
print('{0}-{1}'.format(x, y))
print(f'x: {x}{{显示大括号}}')  # 3.6版加入f-string方法
print('%%d x: %d' % x)  # C format
print('%%(x)d x: %(x)d' % {'x': x})

dict1 = {'name': 'Tony', 'age': '35'}
print('name: {name}, age: {age}'.format(**dict1))
print(f'name: {dict1["name"]}')

lst = ['hello', 'world']
print('{0[0]},{0[1]}'.format(lst))

print('-' * 20, '.format()')
num = 123456
print('{:0>12,.2f}'.format(num))  # 右对齐
print('{:*<12d}'.format(num))  # 左对齐
print('{:*^1,.2f}'.format(num))  # 居中对齐

print('-' * 20, '进制转换')
print('{:b}'.format(5))
print('{:d}'.format(10))
print('{:o}'.format(9))
print('{:x}'.format(15))
print('{:#x}'.format(15))
print('{:#X}'.format(15))
