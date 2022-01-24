#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(3):
    try:
        # assert语句失败将引发AssertionError
        assert i != 1, 'i不能为1'
        print(i)
    except AssertionError as ae:
        print(ae)
        # exit(-1)
    else:
        print('%s OK' % i)
    finally:
        print('结束第%d轮循环\n-----------' % i)

try:
    n = 0
    print(10 / n)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error.')
finally:
    print('Finally.')
print('End')
print('-' * 40)


# 转换异常的类型
try:
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('Convert error type.')
except ValueError as ve:
    print(ve)

