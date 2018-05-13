# -*- coding: utf-8 -*-
#Created on 2018年5月3日
import pymysql

#打开数据库连接
conn = pymysql.connect(host="localhost",user="root",password="root",db="mysql",port=3306)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print(row)
print("MySQL server version:", row[0])
cursor.close()
conn.close()