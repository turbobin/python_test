#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月8日

def parms(*args,**kw):  #可接收任意参数形态的调用
    print(args)
    print(kw)
    
parms([12,3,4],[3,4,5],x=99,d={'a':11,'b':22,'c':33})



#定义一个装饰器
import functools
def log(func):
    @functools.wraps(func)  #恢复函数的__name__等签名属性
    def wrapper(*args,**kw):    #可接受任意参数的调用
        print('call %s():' %func.__name__)  # __name__属性，可以得到函数的名字
        return func(*args,**kw)
    return wrapper

@log        #相当于执行了 now = log(now) ,增强了now()函数
def now():
    print('2018-5-8')
    
now()
print(now.__name__)

#带参数的decorator
def log_parm(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log_parm('excute')
def now_():
    print('2018-05-08')
    
now_()
print(now_.__name__)