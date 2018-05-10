#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月10日

#若要启动大量的子进程，可以用进程池的方式批量创建
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #可以同时跑5个进程，缺省时默认为cpu核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()   #调用close之后就不能添加新的进程了
    p.join()    #会等待所有的子进程执行完毕
    print('All subprocesses done.')
