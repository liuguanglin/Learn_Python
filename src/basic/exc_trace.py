#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import logging


class MyErr(Exception):
    pass


def division(s):
    n = int(s)
    if n == 0:
        raise MyErr('Divisor cannot be %s' % s)
    return 10 / n


def func(x):
    try:
        division(x)
    except MyErr as me:
        print(me)
        traceback.print_exc()
        print('traceback')
    finally:
        print('End func()')


func('0')

print('-' * 40)


def func2(x):
    try:
        division(x)
    except MyErr as me:
        print(me)
        logging.exception(me)
        print('logging...')
    finally:
        print('End func2()')


func2('0')

print('END')
