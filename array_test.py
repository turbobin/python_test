# -*- coding: utf-8 -*-
array = ["a1","d4","c3","e4","b5"]

# ~ 排序
# ~ array.sort() #永久性排序
# ~ print (array)

# ~ array.sort(reverse=True) #按字母倒序排序(反转)
# ~ print (array)

# ~ 临时排序 sorted()
print (sorted(array,reverse=True))
print (array)

# ~ 倒序打印列表
array.reverse()
print (array)

# ~ 确定数组长度
print (len(array))

# ~ 遍历数组
for ele in array:
	print (ele)
