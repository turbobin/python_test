#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日
import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    result = re.match(r'UTC([+-]\d+):00',tz_str)
    time = result.group(1)
    tz_utc = timezone(timedelta(hours=int(time)))
    dt_utc = dt.replace(tzinfo=tz_utc)
    print(tz_utc)
    return  dt_utc.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t1)
print(t2)
assert t1 == 1433121030.0,t1
assert t2 == 1433121030.0,t2
