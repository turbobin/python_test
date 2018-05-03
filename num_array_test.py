# -*- coding: utf-8 -*-
#创建数值列表
for value in range(1,5):	#含头不含尾
	print (value)	#打印1~4

#转换成数组列表
nums = list(range(1,5))
print (nums)

even_nums = list(range(1,11,2)) #指定步长为2
print (even_nums)

#  eg：
squares = []
for value in range(1,11):
	squares.append(value**2)
	
print (squares)

# ~ 对数字进行简单计算
print (min(nums))
print (max(nums))
print (sum(nums))

# ~ 列表解析
squares = [value**2 for value in range(1,11)]
print (squares)

