#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

# 在内存中读写str
f = StringIO()
f.write('hello\n')
f.write('你好')
print(f.getvalue())

f = StringIO('Good\nmorning.')
while (line := f.readline()):
    if line:
        print(line.rstrip())
    else:
        break

# 在内存中读写bytes类型数据
f = BytesIO()
f.write('你好'.encode('utf-8'))
print(f.getvalue().decode('utf-8'))

b_data = '二狗'.encode()
f = BytesIO(b_data)
print(f.read().decode('utf-8'))
