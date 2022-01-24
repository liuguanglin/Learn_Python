#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time

s = 'abc123xyz456'
p = '[a-z]+(\d+)'
r1_start = time.time()
rec = re.compile(p)
for i in range(1_000_000):
    rec.match(s)
r1_end = time.time()
print(r1_end - r1_start)

r2_start = time.time()
for i in range(1_000_000):
    re.match(p, s)
r2_end = time.time()
print(r2_end - r2_start)
