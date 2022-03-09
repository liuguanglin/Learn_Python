#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os

os.chdir('res')
conf_file1 = 'test1.ini'
conf_file2 = 'test2.ini'

cnf = configparser.ConfigParser()
cnf['users'] = {'user1': 'Jeanne', 'user2': '张三'}
cnf.add_section('addr')
cnf.set('addr', 'ip', '192.168.1.5')  # 官方不建议使用get/set等旧式API，应该使用映射协议访问
cnf.set('addr', 'port', '8080')

with open(conf_file1, 'w+') as f:
    cnf.write(f)

print('从文件读取数据:')
file_name = cnf.read(conf_file1)
print('file name: ', file_name)
print('sections: ', cnf.sections())
print('items("users"): ', cnf.items('users'))
print('"User1" in section("users")? ', 'User1' in cnf['users'])  # section中的key不区分大小写
print('Default protocol: ', cnf['addr'].get('proto', 'TCP'))
print('Port data type: ', type(cnf.get('addr', 'port')))  # 默认的数据类型是字符串，可使用getint()、getboolean()等方法转换数据类型

# 修改配置信息
cnf.read(conf_file2)
cnf['users']['user2'] = '李四'
# cnf.set('users', 'user2', '王五')
del cnf['users']['user1']
# cnf.remove_option('users', 'user10')   # 删除不存在的option不报错
del cnf['addr']
# cnf.remove_section('address')  # 删除不存在的section不报错
cnf['groups'] = {'group1': 'Team1'}

with open(conf_file2, 'w') as f:
    cnf.write(f)
print(f'\n数据修改后写入{conf_file2}')
