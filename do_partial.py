#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月8日
import functools

#偏函数
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新函数，
# 这个函数可以固定住原函数的部分参数，从而在调用时更简单

# 如sorted()函数默认按照自然排序，如要默认按照倒序且绝对值排序，则可以定义一个新的函数
# def sorted_desc(arr):
#     return sorted(arr,key=abs,reverse=True)

#上面定义可写成：
sorted_desc = functools.partial(sorted,key=abs,reverse=True)
print(sorted_desc([22,-55,-21,54,-52,62,21]))

