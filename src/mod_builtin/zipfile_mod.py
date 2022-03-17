#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import zipfile
from zipfile import ZipFile


zip_file = 'myfile.zip'
with ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
    # 默认待添加的文件的mtime不能早于1980年
    for root, dirs, files in os.walk('conf.d'):
        for file in files:
            zf.write(os.path.join(root, file))

    # 可将字符串或ZipInfo实例写入文件
    zf.writestr('about.txt', 'It is a zip file.')

    # 可对内部文件进行读写操作
    with zf.open('add.txt', 'w') as myfile:
        myfile.write(b'Add a file')
    zf.comment = '注释\nThis is a comment.'.encode('utf-8')

print(f'Is {zip_file} a zip file? ', zipfile.is_zipfile(zip_file))

with ZipFile(zip_file) as zf:
    print(f'File name: {zf.filename}')
    print(zf.read('about.txt').decode('utf-8'))  # 通过文件名或ZipInfo对象读取文件
    print(f"Comment:\n{zf.comment.decode('utf-8')}")
    print('\nInfo list:')
    print(f'filename  filesize  compress_size')
    for i in zf.infolist():
        print(i.filename, '\t', i.file_size, i.compress_size)
    print('\nName list:\n', zf.namelist())
    print('\nContent list:')
    zf.printdir()
    zf.extractall('dst_path')
    # zf.extract('file', 'path')  # 解压指定文件

# 往压缩包内追加文件
with ZipFile(zip_file, 'a') as zf:
    zf.write('new.txt')


# 命令行操作
# -c 创建压缩文件
# $ python -m zipfile -c myfile.zip src_dir src_file

# -e 解压到指定路径
# $ python -m zipfile -e myfile.zip output_dir

# -l 列出压缩包内的文件
# $ python -m zipfile -l myfile.zip

# -t 测试压缩文件
# $ python -m zipfile -t myfile.zip
