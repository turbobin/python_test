#!/usr/bin/env python
# -*- coding: utf-8 -*-
# msg = "  hello python world  " 
# print (msg.title()) #把每个单词首字母大写
# print (msg.lower()) 
# print (msg.upper()) 
# 
# print(msg.rstrip()) #去除尾部空格
# print(msg.strip())  #去除两端空格
# print(msg.lstrip()) #去除开头的空格
import sys

def test():
    args = sys.argv
    print('args=',args)
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello %s' %args[1].title())
    else:
        raise TypeError("Too many arguments!")

print(__name__)
if __name__ == '__main__':
    test()

