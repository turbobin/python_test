#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月8日

#拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢？
#使用type()
print(type(123))    # <class 'int'>
print(type("hello"))# <class 'str'>
print(type(None))   # <class 'NoneType'>
print(type(abs))   # <class 'builtin_function_or_method'>
print(type(str))   # <class 'type'>

print(type(123) == int) #True
# 判断一个对象是否是函数
import types
def fn():
    pass

print(type(fn)==types.FunctionType) # True
print(type(abs)==types.BuiltinFunctionType) # True
print(type(lambda x: x * x)==types.LambdaType) # True
print(type((x for x in range(10)))==types.GeneratorType) # True

#判断类时，使用isinstence()
#isinstence(stu,Student)   -> True
#isinstence(stu,Person)    -> True

#判断基本类型
print(isinstance(123, (int,str)))       # -> True
print(isinstance("hello", (int,str)))   # -> True
print(isinstance((1,2,3,4), tuple))  # -> True

#使用dir() --获取一个对象的所有属性和方法
#返回一个包含字符串的list
print(dir('abc'))

# 其他：
# hasattr(obj, name)        判断是否有name属性
# setattr(obj, name, value) 设置name属性
# getattr(object, name，404)    获取对象得到name属性，若不存在，返回404

# eg
def readImage(fp):
    if hasattr(fp, "read"):
        return fp.read
    return None

