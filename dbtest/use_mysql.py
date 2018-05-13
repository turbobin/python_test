#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月12日

import pymysql

#打开数据库连接
conn = pymysql.connect(host="localhost",user="root",password="root",db="mysql",port=3306)
cursor = conn.cursor()
cursor.execute("create database if not exists mydatabase;")
cursor.execute('create table if not exists students \
    (id varchar(20) primary key, name varchar(20), score int);')
cursor.execute(r"insert into students values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into students values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into students values ('A-003', 'Lisa', 78)")
conn.commit()

# 执行查询语句
# cursor.execute('select * from students where name =? or id =?',('Adam','A-003'))
cursor.execute("select * from students where name = %s or id = %s",('Adam','A-003'))

results = cursor.fetchall() #将取出所有结果,返回一个二维数组
print(results)
cursor.execute('drop table students;')
cursor.close()
conn.close()
