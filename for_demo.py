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
    
#python中只要是可迭代对象，就可以使用for循环
#如何判断一个对象是否可迭代？
from collections import Iterable

print(isinstance("abc", Iterable))  #str是否可迭代?    ——True
print(isinstance([1,2,3], Iterable))  #list是否可迭代? ——True
print(isinstance(123, Iterable))  #整数是否可迭代?      ——False

#如果要实现下标循环，可以使用enumerate函数把一个list变成索引-元素对
for i,value in enumerate(['a','b','c','d']):
    print(i,value)
    
for x,y in [(3,9),(2,4),(4,16)]:
    print(x,y)
    