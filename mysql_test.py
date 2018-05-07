# -*- coding: utf-8 -*-
#Created on 2018年5月3日
import pymysql

#打开数据库连接
<<<<<<< HEAD
conn = pymysql.connect(host="localhost",user="root",password="root",db="mysql",port=3306)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print("MySQL server version:", row[0])
cursor.close()
conn.close()
=======
db = pymysql.connect(host="localhost",user="root",password="123456",db="test",port=3307)

cur = db.curson()
>>>>>>> 6b91e0f2fd75d0f8a5e200c260c4800179258a34
