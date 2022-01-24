#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

d1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d2 = d1.copy()
d1['k3'] = 'v33'
d1.update({'k4': 'v4', 'k5': 'v5'})
d1['k6'] = 'v6'
print('k1' in d1, '\n')
print('d1.keys()==>', d1.keys(), '\n')
print('d1.values()==>', list(d1.values()), '\n')
print('items():', d1.items())
print(d1.setdefault('k88', 'v88'))
print(d1.get('k100', 100), '\n')
del d1['k1']
print('d1==>', d1)
print('-' * 20)

d3 = dict().fromkeys(list(range(5)), 'dog')
print('d3==>', d3, '\n')

for x, y in enumerate(d1, start=100):
    print('{}, {}'.format(x, y))

print(sorted(d1.items(), key=lambda s: s[1], reverse=True))
print(sorted(d1.items(), key=operator.itemgetter(1), reverse=True))

d1.clear()
del d1
