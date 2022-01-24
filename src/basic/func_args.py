#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fun_args(a1, a2=999, *tup_arg, **dic_arg):
    print('a1=>', a1, ' a2=>', a2)
    for e in tup_arg:
        print(e, end=' ')
    print('\n-----End tuple args-----')
    for k in list(dic_arg.keys()):
        print(f'{k}=> {dic_arg[k]}')
        # print('{0}->{1}'.format(k, dic_arg[k]))
    print('\n' + '-' * 40)


fun_args(1, 888, 'hello', 'world', x=11, y=22, z=33)
fun_args(1, 888, *('hello', 'world'), **{'x': 11, 'y': 22, 'z': 33})


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# '/'左边只能是位置参数，'/'右边只能是关键字参数，二者之间可同时使用这两类参数
def combined_example(pos_only, /, standard, *, kwd_only):
    """
    :param pos_only:
    :param standard:
    :param kwd_only:
    :return:
    """
    print(pos_only, standard, kwd_only)


combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
