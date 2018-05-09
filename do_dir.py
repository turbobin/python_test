#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月9日

#操作文件和目录
import os

print(os.name)  #nt 表示Windows，posix表示mac os/Linux/Unix
print(os.environ)   #显示环境变量
print(os.environ.get('path'))   #获取某个key

# 在某个目录下创建一个新目录
print(os.path.join('C:\\Users\\Administrator\\Desktop','testdir'))