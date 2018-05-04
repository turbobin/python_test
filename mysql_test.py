# -*- coding: utf-8 -*-
#Created on 2018年5月3日
import pymysql

#打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="123456",db="test",port=3307)

cur = db.curson()