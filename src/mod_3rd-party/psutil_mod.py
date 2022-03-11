#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import psutil
from datetime import datetime

print('CPU信息')
print('CPU使用时间: ', psutil.cpu_times())
print('逻辑CPU数量: ', psutil.cpu_count())
print('物理CPU核心数: ', psutil.cpu_count(logical=False))
print('每核CPU使用率: ', psutil.cpu_percent(percpu=True))

print('\n内存信息')
mem = psutil.virtual_memory()
print('总内存(GB): ', mem.total / 1024 / 1024 / 1024)
print('已使用内存(GB): ', mem.used / 1024 / 1024 / 1024)
print('空闲内存(GB): ', mem.free / 1024 / 1024 / 1024)
print('交换空间: ', psutil.swap_memory())

print('\n磁盘信息')
print('分区信息: ', psutil.disk_partitions())
print('使用率: ', psutil.disk_usage('c:\\') if os.name == 'nt' else psutil.disk_usage('/'))
print('磁盘I/O统计: ', psutil.disk_io_counters())

print('\n网络信息')
print('套接字连接信息: ', psutil.net_connections())
print('网络I/O统计: ', psutil.net_io_counters())
print('各网卡I/O统计: ', psutil.net_io_counters(pernic=True))
print('网卡地址: ', psutil.net_if_addrs())
print('网卡信息: ', psutil.net_if_stats())

print('\n系统启动时间: ', datetime.fromtimestamp(psutil.boot_time()))

print('\n进程信息')
print('PID列表: ', psutil.pids())
proc = psutil.Process(os.getpid())
print('进程名: ', proc.name())
print('程序路径: ', proc.exe())
print('当前工作目录: ', proc.cwd())
print('程序命令: ', proc.cmdline())
print('进程状态： ', proc.status())
print('所属用户: ', proc.username())
print('启动时间: ', proc.create_time())
# print(proc.uids())    # POSIX下有效
# print(proc.gids())
print('CPU时间: ', proc.cpu_times())
print('CPU亲和度: ', proc.cpu_affinity())
print('内存占用率: ', proc.memory_percent())
print('内存信息: ', proc.memory_info())
print('打开的文件列表:', proc.open_files())
print('套接字连接: ', proc.connections())
print('线程列表: ', proc.threads())
print('线程数量: ', proc.num_threads())
print('环境变量: ', proc.environ())
# proc.terminate()

print('\n当前在线用户: ', psutil.users())

print('\n电池信息: ', psutil.sensors_battery())

if os.name == 'nt':
    print('Windows service:')
    print(list(psutil.win_service_iter()))
    print(psutil.win_service_get('alg').as_dict())

# print(psutil.test())    # 进程状态
