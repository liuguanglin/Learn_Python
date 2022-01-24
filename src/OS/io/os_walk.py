#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

p = 'res'
os.chdir(p)
for root, dirs, files in os.walk('.'):
    for f in files:
        print(os.path.join(root, f))
    for d in dirs:
        print(os.path.join(root, d))
