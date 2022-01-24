#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

"""
os.O_RDONLY
os.O_WRONLY
os.O_RDWR
os.O_APPEND
os.O_CREAT
os.O_EXCL
os.O_TRUNC

上述常量在 Unix 和 Windows 上均可用。
"""

os.chdir('res')
file = 'os_open.txt'
fd = os.open(file, os.O_RDWR | os.O_CREAT)
os.write(fd, '你好\n'.encode())
file_size = os.path.getsize(fd)
print(f'File size: {file_size}')
os.lseek(fd, 1, 0)
print(os.read(fd, file_size))
os.close(fd)

with open(file, 'rb') as f:
    print(f.read())
