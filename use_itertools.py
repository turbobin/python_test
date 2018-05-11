#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月11日

from collections import Iterator
import itertools
#用于操作迭代对象的函数,返回值是一个Iterator
natuals = itertools.count(1)    #创建一个自然徐序列

cs = itertools.cycle('ABC') #把传入的序列循环重复下去

ns = itertools.repeat('A',3)    #把一个元素无限重复下去，可以限定次数

print(isinstance(natuals, Iterator))
#可根据判断函数根据条件截取一个有限序列
n = itertools.takewhile(lambda x:x <= 10,natuals)
print(list(n))

for c in itertools.chain('abc','xyz'):  #chain()可以把一组迭代对象串联起来，形成更大的迭代器
    print(c)
    
#把相邻的重复元素挑出来放在一起：groupby()
for key, group in itertools.groupby('aaabbccddd'):
    print(key,list(group))    
