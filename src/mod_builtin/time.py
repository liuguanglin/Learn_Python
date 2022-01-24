#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

"""
+────────────────+──────────────+────────────
|                | strptime     |              | localtime gmtime  |            |
|                | ---------->  |              | <----------       |            |
| Format String  | <----------  | struct_time  | ---------->       | Timestamp  |
|                | strftime     |              | mktime            |            |
+────────────────+──────────────+────────────
"""

# 生成struct_time
print('gmtime()==>', time.gmtime())
print('localtime([timestamp])==>', time.localtime())
print('strptime()==>', time.strptime('2017-3-21', '%Y-%m-%d'))
print()

# 生成timestamp
print('time()==>', time.time())
print('mktime()==>', time.mktime(time.localtime()))
print()

# 指定时间格式
print('strftime:', time.strftime('%Y/%m/%d %H:%M:%S'))
print('strftime()==>', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print()

# 生成%a %b %d %H:%M:%S %Y格式的时间
print('ctime()==>', time.ctime(time.time()))
print('asctime()==>', time.asctime(time.localtime()))
