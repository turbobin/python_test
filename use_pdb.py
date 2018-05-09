#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月9日

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 设置一个断点，运行到这里会自动暂停,输入命令p n 查看n变量值，输入c继续执行,输入q结束调试
print(10 / n)
