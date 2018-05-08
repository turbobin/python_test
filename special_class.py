#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月8日

#定制类 __str__    ：为类对象返回一个好看的字符串
class Student():
    def __init__(self,name):
        self.name = name
#         print(self) #<__main__.Student object at 0x011983F0>
        
    def __str__(self):
        return 'Student Object (name %s)' %self.name

s = Student('turtobin')
print(s)    #添加__str__后，按指定字符串返回

#定制类 __iter__    ：将类变成可迭代对象
class Fib():    #定义一个斐波拉契数列
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器a,b
    
    def __iter__(self):     #实现迭代操作
        return self #实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:   #退出循环条件
            raise StopIteration();
        return self.a
    
    def func(self):
        pass
    
    def __getitem__(self,n):    # 实现取下标操作
        a, b = 0, 1
        for x in range(n):
            a, b = b ,a + b
        return a
# n = Fib()
# print(dir(n))
# print(n.__next__())
for n in Fib():
    print(n)
        
f = Fib()
print(f[10])    # 取可迭代对象Fib()下标为10的元素

# __getattr__函数    ：动态的返回一个属性,可用于链式调用
class Chain():
    def __init__(self,url=''):
        self._url = url
        
    def __getattr__(self,url):
        return Chain('%s/%s' %(self._url,url))
    
    def __str__(self):
        return self._url
    
    _repr__ = __str__
    
path = Chain('http://www.baidu.com').news.ChinaNews
print(path)

# 调用实例方法时，可以创建p.show() 调用，也可以定义__call__在实例本身上调用
class Person(object):
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print('My name is %s.' % self.name)

    def __call__(self):
        self.show()

p = Person('Michael')
p.show()    #可以创建实例调用
p()         #也可以用实例本身调用

# 如何判断一个对象是可调用对象？使用callable()
print(callable(Student))    # ->True
print(callable(123))        # ->False
print(callable('str'))        # ->False