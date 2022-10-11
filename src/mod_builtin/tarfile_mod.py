#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO
import tarfile
import time


arc_file = 'mytar.tgz'

with tarfile.open(arc_file, 'w') as tar:
    tar.add('conf.d', 'conf.d.bak')  # 默认可递归添加目录
    # 添加TarInfo对象，可从文件或内存中传入二进制数据
    info = tarfile.TarInfo('notice.txt')
    add_info = '注意\nThis is an archive file.'.encode('utf-8')
    info.size = len(add_info)
    info.mtime = time.time()    # 若不指定mtime，则时间默认为1970-1-1
    tar.addfile(info, BytesIO(add_info))

print(f'Is {arc_file} a tarfile? ', tarfile.is_tarfile(arc_file))
print('tarfile.encoding: ', tarfile.ENCODING)

with tarfile.open(arc_file) as tar:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar)
    # tar.extract('tar/path/file', 'to_path')  # 提取指定文件
    print('tarinfo: ', tar.tarinfo)
    print('tar name: ', tar.name)
    print('getnames():\n', tar.getnames())
    # print(tar.getmembers())
    print('\nmembers:')
    for m in tar.members:
        if m.isdir():
            print(f'{m.name}')
        else:
            print(f'{m.name}  {m.size} bytes')
    print('\ntar.list():')
    tar.list()

# 往非压缩的归档文件中追加文件
with tarfile.open('arcfile.tar', 'a') as tar:
    tar.add('append_file')


# 命令行操作
# -c 创建归档文件
# $ python -m tarfile -c myarc.tar  src_file src_dir

# -e 提取归档文件到指定目录
# $ python -m tarfile -e myarc.tar dst_dir

# -l 列出归档文件中的文件
# $ python -m tarfile -v -l myarc.tar

# -t 测试tarfile是否有效
# $ python -m tarfile -t myarc.tar
