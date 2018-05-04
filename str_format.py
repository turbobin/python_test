#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月3日

#当输出数据有变量时，可是使用格式化字符串的方式
print('hello,%s' %'wolrd')
print('hey,%s,you hava earned $%d.' %('John',10000)) #多个%要使用括号括起来，变量之间逗号隔开
      
"""
%s 表示字符串替换    #可以把任何数据类型转换成字符串
%d 表示整数
%f 表示浮点数
%x 表示十六进制整数
"""
#指定是否补0和整数与小数的位数
print('%2d-%02d.' %(3,1))   #  3-01.
print('%.4f.' %3.1415926535)#3.1416.

#如果要表示%，需要转义，用%%表示
print('you rate:%d %%.' %50)

s = set([1,2,4])
s.add((6,4,5,6))
print(s)
# L = []
# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     L.append(i)
#     
# print(L)