#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月9日

import logging
logging.basicConfig(level=logging.INFO,filename='err.log',filemode='w')  
    #输出日志到文件，'a'表示追加模式，‘w'表示重写

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
