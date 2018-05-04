#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月4日

#位置参数
def calculate(x,n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    print(s)
    
calculate(2,3)
print('--------------------')
#默认参数
def calculate1(x,n=2):  
    #必选参数在前，默认参数在后
    #调用时，可以按顺序提供默认参数，当不按顺序时，必须把参数名写上
    s = 1
    while n > 0:
        n -= 1
        s *= x
    print(s)
    
calculate1(2,1)
calculate1(2)   #省略第二个参数时，使用默认的参数

#注意，当传入一个列表时
# def add_end(L=[]):  #默认参数是一个可变对象，会记录上次的调用
#     L.append('end')
#     return L
def add_end(L=None):  #让默认参数指向不可变对象
    if L is None:
        L=[]
    L.append('end')
    return L 
print(add_end([1,2,3]))
print(add_end()) #-->['end']
print(add_end()) #-->['end', 'end']
print('--------------------')

#可变参数
def hello(greeting, *args): #接收的是一个list
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))
        
hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')