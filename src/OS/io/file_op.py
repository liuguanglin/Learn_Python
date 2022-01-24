#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import time

print('当前路径：' + os.getcwd())
path = r'res'
os.chdir(path)
print('当前路径：' + os.getcwd())
src_file = 'src.txt'
dst_file = 'dst.txt'
str_time = str(time.time())
with open(src_file, 'w') as f:
    f.write('你好')

os.mkdir('a')
os.makedirs('a/b/c')

shutil.copyfile(src_file, dst_file)  # dst必须为目标文件名，若dst存在则覆盖
shutil.copy(src_file, 'a/')  # dst可为目录名，若dst存在则覆盖
shutil.copy2(src_file, dst_file)  # 在copy基础上使用copystat()尽可能复制文件元数据
shutil.copystat(src_file, dst_file)  # 仅复制文件/目录权限、最后访问、修改时间，dst必须已经存在
shutil.copymode(src_file, dst_file)  # 仅复制文件/目录的权限，不复制其内容和所有者，dst必须已经存在
shutil.copytree('a/b', 'a/dir' + str_time)  # 复制目录，dst不能已经存在
os.rename(src_file, str_time + '.txt')  # 重命名文件、目录，dst不能已经存在
shutil.move(dst_file, src_file)  # 移动或重命名文件/目录

time.sleep(5)
# os.rmdir('a')  # 删除一个空目录
os.removedirs('a/b/c')  # 递归删除空目录
shutil.rmtree('a')  # 删除完整的目录树
os.remove(src_file)  # 删除一个文件
# os.unlink(src_file)  # 删除文件，对目录无效

[os.unlink(_) for _ in os.listdir('.') if os.path.splitext(_)[1] == '.txt']
