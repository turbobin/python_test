#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月14日

# 子程序是协程的一种特例，此子程序在内部执行可以中断，
# 转而执行其他子程序，适当的时候返回来接着执行

#生产消费者例子
def consumer():
    r = ''
    while True:
        n = yield r #此处中断，返回消息结果
        print('n:',n)
        if not n:
            return
        print('[COUSUMER] consuming %s...' %n)
        r = '200 OK'
def producer(c):
    c.send(None)    #此语句用于启动生成器
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] producing %s...' %n)
        r = c.send(n)   #切换到consumer执行
        print('[PRODUCER] consumer return: %s' %r)
    c.close()
    
c = consumer()  #返回一个generator
producer(c)