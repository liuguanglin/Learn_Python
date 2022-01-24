#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

path = 'res'
os.chdir(path)
print('Current DIR: ' + os.getcwd())
myfile = 'myfile.txt'

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
f = open(myfile, 'w')
print('f.writable()==>', f.writable())
f.write('Line 1\n')
f.write('Line 2, hello.\n')
f.writelines(['Line 3,你好。\n', 'End'])
f.flush()
f.close()
print('-' * 20, 'Write done.')

print('f.read()')
with open(myfile, 'r') as f:
    print('f.readable()==>', f.readable())
    print(f.read())
print('f.closed==>', f.closed)

print('-' * 20)
print('f.read(size)')
total_size = os.path.getsize(myfile)
read_size = 0
n = 10
with open(myfile, 'r') as f:
    while read_size < total_size:
        print(f.read(n))
        read_size += n

print('-' * 20)
print('f.readline()')
with open(myfile, 'r') as f:
    while f.tell() < total_size:
        line = f.readline()
        print(line.rstrip('\n'))

print('-' * 20)
print('f.readlines()')
with open(myfile, 'r') as f:
    print(f.readlines())
