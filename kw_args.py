#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月4日

#关键字参数
def print_scores(**kw): #接收的是一个dict
    print(' Name Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s %d' % (name, score))
        print()
print_scores(Adam=99, Lisa=88, Bart=77)
data = {
'Adam Lee': 99,
'Lisa S': 88,
'F.Bart': 77
}
print_scores(**data)

#限制关键字参数的名字可以使用：
# 命名关键字参数-- *后面分割的参数，调用时必须传入参数名，如果有参数有默认值可以省略
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print(' Name: %s' % name)
    print(' Gender: %s' % gender)
    print(' City: %s' % city)
    print(' Age: %s' % age)
    print()
    
print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
