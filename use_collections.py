#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) #可以创建一个自定义的tuple对象
p = Point(1, 2)
print('Point:', p.x, p.y)
#类似的，要用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x','y','r'])

#list按索引访问很快，但是插入和删除很慢,deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')   #往头部添加元素，popleft():从头部删除元素
print(q)


from collections import defaultdict

dd = defaultdict(lambda: 'N/A') #定义一个函数，当key不存在时返回默认值,除了这个功能其他和dict一样
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1']) # ->'abc'
print('dd[\'key2\'] =', dd['key2']) # ->N/A

# 使用dict时，Key是无序的，如果要保证key的顺序（插入顺序）可以使用Ordereddict
from collections import OrderedDict
d = dict([('b',2),('c',1),('a',3)])
od = OrderedDict(d)
print('d:',d)
print('od:',od)
for key,value in od.items():
    print(key,value)

#计数器，如 统计一个字符出现的次数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

