#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月7日

#高阶函数：一个函数可以接收另一个函数作为参数

def add(x,y,f):
    return f(x) + f(y)

x, y = -5, 6
f = abs # 绝对值函数abs() 赋给f变量
print (add(x,y,f))

#map()函数 ——>一个高阶函数
def f(x):
    return x * x

r = map(f,[1,2,3,4,5])  #将函数依次作用到每个元素上，结果是一个Iterator

print(list(r))

# eg:将数字列表全部变成字符串
print(list(map(str,[1,2,3,4,5])))

#reduce()函数 ——>把结果不断和下一个元素做累积计算
from functools import reduce
def sum_2(x,y):
    return x * y

r = reduce(sum_2,[1,2,3,4,5])
print('sum:',r)

# filter() ——>用于过滤序列，和map()类似，不同的是，filter把传入的函数依次作用于每个元素，
# 根据返回值是True还是False决定是否保留元素
#如 过滤非首字母大写的字符串
def _not_title(s):
    return s == s.title()

re = list(filter(_not_title,["java","C++","Python","php"]))
print(re)

# sorted()函数
arr = [21,44,-52,12,-24]
print(sorted(arr,key=abs))  #key函数来实现自定义的排序，临时排序，不会改变原来arr的顺序

# 倒序排列
print(sorted(arr,key=abs,reverse=True))
