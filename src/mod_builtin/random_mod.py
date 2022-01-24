#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print('random()==>')
for i in range(5):
    print(random.random(), end=' ')

print('\n\nuniform()==>')
for i in range(5):
    print(random.uniform(10, 12), end=' ')

print('\n\nrandint()==>')
for i in range(5):
    print(random.randint(10, 12), end=' ')

print('\n\nrandrange()==>')
for i in range(5):
    print(random.randrange(10, 14, 2), end=' ')

print('\n\nchoice()==>')
for i in range(5):
    print(random.choice('Hello'), end=' ')

print('\n\nshuffle()==>')
lst = [x for x in range(10)]
random.shuffle(lst)
print(lst)

print('\n\nsample()==>')
lst = [x for x in range(10)]
print(random.sample(lst, 5))
print(lst)
