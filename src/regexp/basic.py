#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

str1 = 'Tom-25'
pm = '(\w\w(\w))-(\d{2})'
ps = '(\w)-(\d)\d'
m = re.match(pm, str1)
s = re.search(ps, str1)
if m:
    print('m.group()=> ', m.group())
    print('m.group(0)=> ', m.group(0))
    print('m.group(1)=> ', m.group(1))
    print('m.group(3)=> ', m.group(3))
    print('m.groups()=> ', m.groups())
else:
    print('No match.')

print('-' * 20, 'search')
if s:
    print('s.group()=> ', s.group())
    print('s.groups()=> ', s.groups())
else:
    print('Search nothing.')

print('-' * 20, 'greedy')
print(re.match('(.*)(\w{2})', str1).groups())
print(re.match('(.*?)(\w{2})', str1).groups())

print('-' * 20, 'group name')
m_dict = re.search('(?P<name>\w+)-(?P<age>\w+)', str1)
print(m_dict.groupdict())

print('-' * 20, 'find')
print('re.findall==> ', re.findall('\w+', str1))  # 返回列表
print('re.finditer==> ', re.finditer('\w+', str1))  # 返回迭代器

print('-' * 20, 'split')
s = 'a,b;;c  d'
p = '[,;\s]+'
# p = ',|;+|\s+'
print(re.split(p, s))
print(re.split(p, s, 2))

print('-' * 20, 'replace')
print(re.sub('-+', 'OK', 'Hi -. Hi --.'))
print(re.subn('-+', 'OK', 'Hi -. Hi --.'))
