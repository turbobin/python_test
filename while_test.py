# -*- coding: utf-8 -*-
# ~ guess_num = int(guess_num)
guess_num = input("Tell me a number,guess you are right or not:\n")
num = "34"
flag = True
while flag:
	if guess_num == "quit":
		break	# break退出整个循环
		
	if guess_num > num:
		guess_num = input("Too large,Guess again:\n")
		# ~ guess_num = int(guess_num)
	if guess_num < num:
		guess_num = input("Too Low,Guess again:\n")
		# ~ guess_num = int(guess_num)
	if guess_num == num:
		flag = "That is it,you are right!\n"
		flag += "do you want to play again?(Y/N)\n"
		guess_num = input(flag)
		if guess_num.lower() == "y":
			guess_num = input("Tell me a number,guess you are right or not:\n")
			continue	#返回到循环开头
		else:
			flag = False		#退出整个循环
		

