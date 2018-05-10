#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日

import random,time,threading

# print(random.random())    #小于1的随机小数
# print(random.randint(1,10))#在指定范围内的随机整数
def loop():
    print('thread %s is running...' %threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s --->%d' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s end.' % threading.current_thread().name)
    
print('thread %s is running...' %threading.current_thread().name)   #主线程开启
t1 = threading.Thread(target=loop,name='Thread-1')  #name缺省时也是Thread-1，Thread-2
t2 = threading.Thread(target=loop,name='Thread-2')
t1.start()  #子线程1开启
t2.start()  #子线程2开启
t1.join()   #等待线程1全部执行完
t2.join()   #等待线程2全部执行完
print('thread %s end.' % threading.current_thread().name)