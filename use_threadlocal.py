#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日
import threading

#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问问题。
class Student():
    def __init__(self,name):
        self.name = name
    
# 创建全局ThreadLocal对象:
local_school = threading.local()    #可以理解为一个dict，绑定的变量是dict中的一个key

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std.name, threading.current_thread().name))

def process_thread(name):
    s = Student(name)
    # 绑定ThreadLocal的student:
    local_school.student = s    #把对象绑定到ThreadLocal
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()