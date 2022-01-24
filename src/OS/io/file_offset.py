#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

"""
f.seek(offset, whence) 
offset表示偏移量，whennce表示参考点，默认为0，表示文件开头，1表示当前位置，2表示文件末尾。
若文件打开为text模式，whence只能为0。
"""

path = 'res'
os.chdir(path)
print('Current DIR: ' + os.getcwd())

myfile = 'offset.txt'
with open(myfile, 'wb') as f:
    f.write('0123456789\n'.encode())
    f.write('abcABC\n'.encode())
    f.write('你好'.encode())

print('File size:', os.path.getsize(myfile))

with open(myfile, 'rb+') as f:
    print('Initial position:', f.tell())
    print(f.read(5))
    print('Position after read(5):', f.tell())
    print('seek(5):', f.seek(5, 1))
    print(f.read(6))
    f.seek(-3, 2)
    print('seek(-3, 2):', f.tell())
    print(f.read(3).decode())
    # truncate([size])截断文件为size个字符，若不指定size，则删除当前位置之后的所有内容
    f.truncate(5)
    f.seek(2)
    f.truncate()
    f.seek(0)
    print(f.read())
