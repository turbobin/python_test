# -*- coding: utf-8 -*-
# ~ 读取文件

file_name = "C:/Users/Administrator/Desktop/douban.txt"
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

print ("-------------------------------------")

with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())
		
print ("-------------------------------------")

with open(file_name) as file_object:
	"""
	readline():读取一行
	readlines():读取全部内容到一个列表（数组）中
	"""
	lines = file_object.readlines()
	
for line in lines:
	print (line.rstrip())
print (lines)

