#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import filecmp

filecmp.clear_cache()
# 默认shallow为True，此时若os.stat()相同，则认为文件相等，而不再比较文件内容。
print(filecmp.cmp('a.txt', 'b.txt'))

cfiles = filecmp.cmpfiles('dir1', 'dir2', ['a.txt', 'b.txt', 'dira2/a.txt'])
print('Common:', cfiles[0])
print('Differ:', cfiles[1])
print('Funny:', cfiles[2])

dcmp = filecmp.dircmp('dir1', 'dir2', ignore=['xxx.txt'])
print('DEFAULT_IGNORES: ', filecmp.DEFAULT_IGNORES)
print('Report:')
print(dcmp.report())
print('\nReport_partial_closure:')
print(dcmp.report_partial_closure())
print('-' * 20)
print('\nReport_full_closure:')
print(dcmp.report_full_closure())
print('-' * 20)
print('\nDiff files: ', dcmp.diff_files)
print('Common files: ', dcmp.common_files)
print('Common dirs: ', dcmp.common_dirs)
print('Common: ', dcmp.common)
print(dcmp.subdirs)  # 将common_dirs映射成value为dircmp对象的字典
print('-' * 20)


print('显示目录中的差异文件:')
def cmp_dir(dircmp):
    if dircmp.left_only:
        print('Left only: ', dircmp.left, dircmp.left_only)
    if dircmp.right_only:
        print('Right only: ', dircmp.right, dircmp.right_only)
    if dircmp.diff_files:
        print('Diff files: ', dircmp.left, dircmp.right, dircmp.diff_files)
    for sdir in dircmp.subdirs.values():
        cmp_dir(sdir)


dc = filecmp.dircmp('dir1', 'dir2')
cmp_dir(dc)
