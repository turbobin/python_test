#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月8日

#给类创建实例后可以给类绑定任何属性和方法，使用__slots__可以限制实例的属性
class Student():
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99    # ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()   
g.score = 99
print('g.score =', g.score)

# 给实例g绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
g.set_age = MethodType(set_age,g)  #给实例绑定一个方法
g.set_age(25)
print(g.age)