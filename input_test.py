# -*- coding: utf-8 -*-
prompt = "Now let me ask you a question"
prompt += "\nwhat is your name?\n"
# ~ name = input("Please enter your name:")
name = input(prompt)
print ("Hello,"+name)

age = input("How old are you?\n")
# ~ print ("your age is:"+age) #字符串
age = int(age)	#转化为数字类型

if age >= 18:
	print ("you have growed up！")
