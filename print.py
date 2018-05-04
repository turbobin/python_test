# -*- coding: utf-8 -*-
#Created on 2018年4月28日

#首字母大写
print("hello world!".title())
#多行内容打印
print("""line1
line2
line3""")

#转义和非转义打印
print('I\'m OK')
print(r'I\'m OK')   #r''里字符串不会做转义

#除法运算
print(10 / 3) #计算结果永远为浮点数，精确
print(10 // 3) #地板除，计算结果永远为整数，只取结果的整数部分
print(10 % 3) #取余数