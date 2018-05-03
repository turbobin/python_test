# -*- coding: utf-8 -*-
# 迭代练习
d ={'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)  # a b c

for value in d.values():
    print(value)    # 1 2 3
    
for key,v in d.items():
    print(key,v)
    
#字符串也可用于迭代
for ch in "hello":
    print(ch)
    
#如何判断一个对象是否是可迭代对象？
from collections import Iterable

print(isinstance('abc', Iterable)) # str是否可迭代    返回True

print(isinstance(123, Iterable)) # 整数是否可迭代    返回False

# 对元素实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)