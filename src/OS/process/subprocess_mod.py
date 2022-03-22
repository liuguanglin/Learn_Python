#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

proc_run = subprocess.run(['hostname'],
                          shell=True,
                          capture_output=True,
                          check=True,
                          text=True)
print(proc_run.__dict__)
print(proc_run.stdout)


proc_popen = subprocess.Popen('nslookup',
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True,
                              text=True)
# out, err = proc_popen.communicate('set type=mx\nw3c.org\n')
# print(out)
proc_popen.stdin.write('set type=cname\n')
proc_popen.stdin.write('www.ietf.org\n')
proc_popen.stdin.close()

print(proc_popen.stdout.read())
print(proc_popen.stderr.read())
proc_popen.stdout.close()
proc_popen.stderr.close()
print(proc_popen.returncode)
print(proc_popen.pid)
print(proc_popen.poll())


print('通过管道传递数据')
p1 = subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'inet'],
                      stdin=p1.stdout,
                      stdout=subprocess.PIPE,
                      text=True)
p1.stdout.close()
print(p2.stdout.read())
# print(p2.communicate()[0])


# 旧的高阶API
proc_call = subprocess.call('hostname', shell=True)
print('Return code: ', proc_call)

try:
    proc_ckcall = subprocess.check_call('hostname', shell=True)
except subprocess.CalledProcessError as e:
    print('Error return code:', e.returncode)
else:
    print('Normal return code:', proc_ckcall)

try:
    proc_ckout = subprocess.check_output('hostname', shell=True, stderr=subprocess.STDOUT, text=True)
except subprocess.CalledProcessError as e:
    print(e.returncode, e.output)
else:
    print(proc_ckout)


# 旧版函数
print(subprocess.getstatusoutput('hostname'))
print(subprocess.getoutput('hostname'))  # 忽略退出码
