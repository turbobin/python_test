#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月12日

import os, sqlite3

print(__file__)
# 首次创建
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
# db_file = 'test.db'
# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table if not exists user \
    (id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()

# 执行查询语句
cursor.execute('select * from user where name =? or id =?',('Adam','A-003'))
# values1 = cursor.fetchone()#将只取出第一条结果，返回一个tuple
# print(values1)
values2 = cursor.fetchall() #将取出所有结果,返回一个list
print(values2)
cursor.close()
conn.close()