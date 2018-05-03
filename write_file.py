# -*- coding: utf-8 -*-

# ~ 写入文件
filename = "write.txt"
with open(filename,'w') as file_object:	#写入模式，文件不存在将创建出来
	file_object.write("this is a writing test.")

with open(filename,'a') as file_object:	#附加模式，将在末尾追加。文件不存在将创建出来
	file_object.write("\nHow do learn?\n")

# ~ 异常
# ~ try:
	# ~ with open("1.txt") as f_object:
		# ~ contents = f.object.read()
# ~ except FileNotFoundError:
	# ~ print ("Sorry,the file 1.txt does not exist.")
	
filename = "Alice.txt"
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	print ("Sorry,the file "+filename+" does not exist.")
else:
	# ~ 计算文件大致包含多少个单词
	words = contents.split()	#分裂成数组
	num_words = len(words) #获取数组长度
	words_cnt = contents.count("Alice")	#统计某个单词出现的次数
	print ("The file "+filename+" has abort "+str(num_words)+" words")
	print ("Alice appears "+str(words_cnt)+ " times")
	
