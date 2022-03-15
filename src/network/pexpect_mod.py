#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
from pexpect.pxssh import pxssh
import sys

# child = pexpect.spawn('ls -l', timeout=5, logfile=sys.stdout, cwd='/home', encoding='utf-8')
child = pexpect.spawn('echo "how are you"', encoding='utf-8')
spawn_log = open('spawn.log', 'w')
child.logfile = spawn_log
# 将日志输出到标准输出
# child.logfile = sys.stdout
# child.expect('(?i)are') # 忽略大小写
print('index: ', child.expect(['one', 'two', 're']))
print('匹配成功前的内容: ', child.before)
print('匹配到的正则表达式的实例: ', child.match)
print('匹配到的关键字: ', child.after)
spawn_log.close()

# pexpect不能解析shell中的管道、重定向等特殊字符，以上特殊字符需要shell自身处理
child = pexpect.spawn('sh -c "ls |xargs file"')
# child = pexpect.spawn('sh', args=['-c', 'ls |xargs file'])
child.expect(pexpect.EOF)
print(child.before.decode())

child = pexpect.spawn('ssh node2', encoding='utf-8')
child.expect('password:')
child.sendline('1234')
# child.send('1234\r')
# child.sendcontrol('c')  # 发送控制信号Ctrl+C
child.expect(']\$')
print(child.before)
child.interact()  # 将控制权交给用户，默认输入"^]"返回程序
child.sendline('exit')


pexpect.run('scp myfile node2:.', events={'(?i)password:': '1234\r', 'yes': 'yes\r'}, logfile=sys.stdout,
            encoding='utf-8')


myssh = pxssh()
myssh.login('node2', 'root', '1234')
myssh.sendline('ls -l')
myssh.prompt()
print(myssh.before.decode())
myssh.sendline('df -Th')
myssh.prompt()
print(myssh.before.decode())
myssh.logout()
