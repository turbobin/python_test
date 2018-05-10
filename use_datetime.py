#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日
from datetime import datetime,timedelta,timezone


#获取当前时间
now = datetime.now()
print(now)
print('type(now):',type(now))

#获取指定日期和时间
dt = datetime(2018,4,9,12,12,44)
print(dt)

#timestamp,时间戳，表示1970年1月1日 UTC+00：00时区到现在为止经过的秒数

#datetime转换为timestamp
print('datetime-->timestamp:',dt.timestamp())
#timestame转换为datetime：使用fromtimestamp
t = 1468454002.0
print('datetime-->timestamp:',datetime.fromtimestamp(t))    #本地时间
print('datetime-->UTCtimestamp:',datetime.utcfromtimestamp(t))    #标准UTC时间

# str转换为datetime，使用strptime函数
cday = datetime.strptime('2018-4-5 18:15:59','%Y-%m-%d %H:%M:%S')
print('str-->datetime:',cday)

#datetime转换为str，使用strftime函数
print(now.strftime('%a, %b %d %H:%M'))

#日期加减:使用timedelta
tm = now + timedelta(hours=10)
print('now + 10h:',tm)
tm = now - timedelta(days=1,hours=10)
print('now - 1 day:',tm)
print(timedelta(hours=10,days=1))   #1 day, 10:00:00

#时区属性：tzinfo，默认为None
tz_utc_8 = timezone(timedelta(hours=8)) #创建时区
print(tz_utc_8) #UTC+08:00
dt = datetime.now().replace(tzinfo=tz_utc_8)    #强制设置为UTC+08:00
print(dt)

#时区转换：可以先通过utcnow()拿到当前UTC时间，再转换为任意时区的时间
#拿到当前UTC时间，并强制设置时区为UTC+00:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

#astimezone
