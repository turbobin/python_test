# -*- coding: utf-8 -*-
array = ["a1","a2","a3","a4","a5"]

#查询
print (array[0])	#打印列表第一个元素
print (array[-1])	#打印列表倒数第一个元素

#修改
array[1]="b2"
print (array)

#添加	append() 	insert()
array.append("a6")	#在末尾添加元素
print (array)

array.insert(1,"c2")#在下标1后插入元素
array.insert(4,"d1")#在下标1后插入元素
print(array)

#删除 del
del array[2]
print(array)

#取出元素		pop()
last_ele = array.pop()
print (last_ele)
print (array)	#列表中元素少一个

first_ele = array.pop(0)
print (first_ele)
print (array)

#移除指定值
array.remove("a3")
print (array)

