#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

intab = 'abc'
outtab = '123'
trantab = str.maketrans(intab, outtab)
str1 = 'It is a cat!'
print('translate==>', str1.translate(trantab))
print('ascii_letters==>', string.ascii_letters)
print('ascii_lowercase==>', string.ascii_lowercase)
print('ascii_uppercase==>', string.ascii_uppercase)
print('digits==>', string.digits)
print('hexdigits==>', string.hexdigits)
print('octdigits==>', string.octdigits)
print('punctuation==>', string.punctuation)
print('printable==>', string.printable)
print('whitespace==>', list(string.whitespace))
print('-' * 20)
tpl = string.Template('Hello,${name}.')
str_map = {'name': 'Tom'}
print(tpl.substitute(str_map))
