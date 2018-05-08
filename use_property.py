#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月8日

#如果一个类属性不能直接访问，一般要在类中定义setxxx和getxxx方法
#python内置装饰器@property可以把一个方法变成属性调用
#@property本身又创建了另一个装饰器@score.setter，提供给属性赋值
class Student():

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
    @property
    def level(self):
        if self._score > 80:
            return 'level A' 
        elif self._score < 60:
            return 'level C'
        else:
            return 'level B'
        
#上面score是可读写属性,level是只读属性
s = Student()
s.score = 60
print('s.score =', s.score)
print('s.level=',s.level)
s.score = 9999
# ValueError: score must between 0 ~ 100!