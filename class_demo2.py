#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月8日
class Student():
    
    def __init__(self, name, score):
        self.__name = name  # __ 表示将name变量私有化，相当于private
        self.score = score

lisa = Student("Lisa Chen",88)
mary = Student("Mary he",85)
# print(lisa.name)    #访问受限制，其实python已将name改名了
print(lisa._Student__name)  #已将name改成_Student__name
print(lisa.score)
age = 23
# print(mary.age)   # 实例变量可以绑定任何数据，但是没有改变类变量
print(age)

#获取对象信息
# 使用type()
print(type(lisa))
print(type(mary))

