#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import date, time, datetime, timedelta, timezone
import time as time0
from pytz import timezone as ptz

# date类
print(date.min, date.max, date.resolution)
print('date.today():', date.today())
print('date.fromtimestamp():', date.fromtimestamp(time0.time()))
d1 = date(2017, 3, 10)
print(d1.year, d1.month)
d2 = d1.replace(year=2022, month=12)
print(d2)
print('timetuple():', d2.timetuple())
print('weekday():', d2.weekday())  # 周一为0
print('isoweekday()', d2.isoweekday())
print('isocalendar():', d2.isocalendar())
print('isoformat():', d2.isoformat())
print('strftime():', d2.strftime('%Y-%m-%d %H:%M:%S'))
print(d2.ctime())
print()

# time类
print('time.min max resolution:', time.min, time.max, time.resolution)
t1 = time(1, 2, 25, 999999)
print(t1.hour, t1.minute, t1.second, t1.microsecond)
print(t1.tzinfo)
t2 = t1.replace(hour=12, minute=23)
print('time.isoformat():', t2.isoformat())
print('time.strftime()', t2.strftime('%Y-%m-%d %H:%M:%S'))
print()

# datetime类
print('today():', datetime.today())
print('now():', datetime.now())
print('utcnow():', datetime.utcnow())
print('fromtimestamp():', datetime.fromtimestamp(time0.time()))
print('utcfromtimestamp', datetime.utcfromtimestamp(time0.time()))
print('strptime():', datetime.strptime('2018-8-8 20:36:01', '%Y-%m-%d %H:%M:%S'))
print('combine():', datetime.combine(date.today(), time(1, 2, 3)))

dt = datetime(2021, 1, 2, 13, 5, 12)
print(dt.year, dt.hour)
print(dt.date(), dt.time())
dt2 = dt.replace(year=2018, hour=16)
print('datetime.timetuple():', dt2.timetuple())
print(dt2.utctimetuple())
print(dt2.toordinal())
print('datetime.weekday() isocalendar() isoformat --- ctime()', dt2.weekday(), dt2.isocalendar(), dt2.isoformat(),
      '----', dt2.ctime())
print('datetime.strftime():', dt2.strftime('%Y/%m/%d %H:%M:%S'))
print()

# timedelta类
now = datetime.now()
dt1 = now + timedelta(days=2, hours=1)
dt2 = now + timedelta(days=-1, hours=-1)
dt3 = now - timedelta(days=1, hours=1)
print(f'now: {now}\ndt1: {dt1}\ndt2: {dt2}\ndt3: {dt3}')
dt_diff = dt1 - dt2
print('dt_diff:', dt_diff)
print('dt_diff.days: {0}\ndt_diff.seconds: {1}\ndt_diff.total_seconds: {2}'.format(dt_diff.days, dt_diff.seconds,
                                                                                   dt_diff.total_seconds()))
print()

# 时区转换
local_tz = ptz('Asia/Shanghai')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
print(utc_dt.astimezone(local_tz))
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 时区之间直接转换
print(tokyo_dt2)
