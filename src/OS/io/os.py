#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print('os.name==>', os.name)
print('os.sep==>', os.sep)
print('os.linesep==>', os.linesep)
print('os.getcwd()==>', os.getcwd())
print('os.path.abspath()==>', os.path.abspath('.'))
print('os.curdir==>', os.curdir)
print("os.listdir('.')==>", os.listdir('.'))
print('os.stat()==>', os.stat(os.getcwd()))
print('-' * 20)
file = r'x:\a\b\c.txt'
print('os.path.basename()==>', os.path.basename(file))
print('os.path.dirname()==>', os.path.dirname(file))
print('os.path.normpath()==>', os.path.normpath(file))
print('os.path.isabs()==>', os.path.isabs(file))
print('os.path.isdir()==>', os.path.isdir(r'D:'))
print('os.path.isfile()', os.path.isfile(r'c:\windows\hh.exe'))
print('os.path.exists()', os.path.exists('D:'))
print('os.path.getsize', os.path.getsize(r'os.py'))
print('os.path.join()==>', os.path.join(r'x:\a', r'b\c.txt'))
print('os.path.split()==>', os.path.split(file))
print('os.path.splitext', os.path.splitext(file))

print('-' * 20, 'Environment variable')
os.environ['py1'] = 'PythonEnv'
print("os.environ['py1']==>", os.environ['py1'])
print('os.putenv()==>')
os.putenv('py1', 'myPython')  # 该方法设置的环境对当前进程无效
os.system('echo py1:%py1%')
print("os.getenv('py1')==>", os.getenv('py1'))
