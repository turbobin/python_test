#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on 2018年5月4日
print("重点——列表生成式:")    
# 列表生成式（list）
L = [x * x for x in range(1,11)]
print(L)

# 两层循环,可以生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 判断条件，生成新的列表
L1 = ['java','python',None,'php',14,'c++']
L2 = [s.title() for s in L1 if isinstance(s, str)]  #筛选出字符串类型生成列表
print(L2)

# 生成器(generator)，一边循环一边计算,保存的是算法
# 写法，只需把[]改成()
print("\n生成器:")    
g = (x * x for x in range(1,11))
print(g)    # 返回一个generator对象 ：<generator object <genexpr> at 0x0061F8A0>

# 可以用迭代方法获取元素
for i in g:
    print(i)

# 
def fib(max_):  #加_用于区分python关键字
    n, a, b = 0, 0, 1
    while n < max_:
        yield b     
        # 把函数变成了一个generator；yield表示中断，当遇到yield语句时返回，再次执行时从yield处继续执行
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib(6)  #返回一个generator对象：<generator object fib at 0x0055F8A0> 

# for i in f: #同样可使用迭代来获取元素
#     print(i)

# 如果要拿到return语句的返回值,需要捕获StopIteration异常
while True:
    try:
        x = next(f)
        print ("f:",x)
    except StopIteration as e:
        print(e.value)
        break
    
it = iter([1,2,3,4])    #iter()函数 将对象生成一个迭代器

"""
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
可以使用isinstance()判断一个对象是否是Iterator对象，注意区分Iterable
for循环本质上就是不断调用next()函数实现的
"""
