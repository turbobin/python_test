#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月8日
def count():
    fs = []
    for i in range(1,4):
        def f():        #函数里面内容不会立刻被执行
            return i * i
        fs.append(f)
        
    print(fs)
    return fs

f1, f2, f3 = count()
# [<function count.<locals>.f at 0x009DD810>, <function count.<locals>.f at 0x01750A98>, <function count.<locals>.f at 0x01750CD8>] 
print(f1)   # ——> <function count.<locals>.f at 0x0062D810>, 返回的函数没有直接执行
print(f1()) # ——> 9,直接调用f之后才执行
print(f2()) # ——> 9,直接调用f之后才执行
print(f3()) # ——> 9,直接调用f之后才执行


# 匿名函数：lambda, 有一个限制：只能有一个表达式
print('\n匿名函数')
def f(x, y):
    return x + y

from functools import reduce
r = reduce(f,[1,2,3,4,5])
print('r=',r)

#上述可改为：
r = reduce(lambda x,y:x + y,[1,2,3,4,5])
print('\n匿名函数结果，r=',r)
