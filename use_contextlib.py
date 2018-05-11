#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月11日
from contextlib import contextmanager
#实现上下文操作，@contextmanager装饰器，with操作语句
class Query():
    def __init__(self,name):
        self.name = name
        
    def query(self):
        print('Query info about %s...' %self.name)
@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('End')
    
search = Query.query

def search_name(self):
    search(self)
    print('search %s...' %self.name)
    
Query.query = search_name
q = Query('Bob')
q.query()

print('\n----------------------')
with create_query('Tom') as qe:     #先执行yield之前的语句，再执行with中的语句，最后执行yield之后的语句
    qe.query()
    
# 如果一个对象没有实现上下文，就不能使用with语句，可以使用closing()把任意对象变成上下文对象
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)
