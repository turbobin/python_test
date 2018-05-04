#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月3日

#单个字符的编码，ord()函数可获取字符的整数表示，chr()函数把编码转换成对应的字符
print(ord('a'))
print(ord('好'))

print(chr(65))
print(chr(20013)) #4e2d

#十六进制表示
print('\u4e2d\u6587')

#bytes类型的数据
s = b'abc'
print(s)

#将str编码为指定的bytes，使用encode()方法
s = 'ABC'.encode('ascii')
print(s)    # b'ABC'

s= '中文'.encode(encoding='utf_8', errors='strict')   # b'\xe4\xb8\xad\xe6\x96\x87'
print(s)

#将bytes变为str，使用decode()方法
print(b'ABC'.decode())
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())

#注：len()函数，如果是str，计算的是字符数，如果是bytes，计算的是字节数