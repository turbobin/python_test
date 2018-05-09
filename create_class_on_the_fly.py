#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月9日

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
#type()函数除了可以查看一个变量的类型，还可以动态的创建一个类
# 需传入3个参数：class名称，继承的父类或集合（多继承），class的方法名称与函数绑定
h = Hello()
print('call h.hello():')
h.hello()   #将fn绑定在方法名hello上
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))
