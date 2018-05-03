#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 

import methon_test

unprint_eles = ["b1","b2","b5","b4"]
printed_eles = []
print ('\n以下是调用import导入模块方法')
methon_test.print_eles(unprint_eles,printed_eles)

# ~ 只导入特定的方法
from methon_test import make_pizza

make_pizza(14,'榴莲披萨','肉松披萨','香菇披萨')

# ~ 指定别名
import methon_test as mt
mt.make_pizza(15,'鸡肉')

# ~ 导入模块中所有函数(不推荐，以防函数重名覆盖)
from methon_test import *
print_eles(['c1','c3','c2'],[])
