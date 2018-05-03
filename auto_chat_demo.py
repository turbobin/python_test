#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  auto_chat.py
#  
from wxpy import *
bot = Bot(cache_path=True)
# ~ bot.file_helper.send("hello")

# ~ @bot.register()
# ~ def print_message(msg):
	# ~ print (msg.text)
	# ~ return msg.text
	
# ~ #进入Python命令行，让程序保持运行
# ~ embed()

friends_stat = bot.friends().stats()

friend_loc = [] # 每一个元素是一个二元列表，分别存储地区和人数信息
for province, count in friends_stat["province"].items():
    if province != "":
        friend_loc.append([province, count])

# 对人数倒序排序
friend_loc.sort(key=lambda x: x[1], reverse=True)

# 打印人数最多的10个地区
for item in friend_loc[:10]:
    print (item[0], item[1])

for sex,count in friends_stat["sex"].items():
	if sex == 1:
		print ("\n男 %d"	% count)
	elif sex == 2:
		print ("女 %d" % count)
		
