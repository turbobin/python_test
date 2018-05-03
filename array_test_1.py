# ~ 切片(提取部分元素)
array = ["a1","a2","a3","a4","a5"]
print ("\n"+str(array[0:3]))
print (array[1:4])
print (array[:4])
print (array[2:])
print (array[-3:])	#从倒数第3个开始

for ele in array[:3]:
	print (ele)
	
# ~ 复制一个列表
another_array = array[:]	#复制了一个列表副本
# ~ another_array = array	#两个变量共享一个数组
another_array.append("a6")	#不影响原来的数组
print (another_array)
print (array)

# ~ 元组(不可修改的列表)
list_a = (34,21,51,11)	#用圆括号表示
# ~ print (list_a[0])
for list_get in list_a:
	print (list_get)

# ~ list_a[0] = 44
# ~ print (list_a)	#报错，不允许修改

list_b = list_a[:2]
print (list_b)
