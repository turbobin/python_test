# -*- coding: utf-8 -*-
import json
filename = "user.json"

# ~ try:
	# ~ with open(filename) as f_obj:
		# ~ username = json.load(f_obj)
# ~ except FileNotFoundError:
	# ~ username = input("请输入用户名:\n")
	# ~ with open(filename,'w') as f_obj:
		# ~ json.dump(username,f_obj)
# ~ else:
	# ~ print ("Welcome,"+username+"!")


# ~ 重构：使代码更具扩展性
def get_stored_username():
	"""
	如果存储了用户名就获取它
	"""
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""
	提示用户输入用户名
	"""
	username = input("请输入用户名:\n")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username
	
	
def greet_user():
	username = get_stored_username()
	if username:
		print ("Welcome,"+username+" !")
	else:
		username = get_new_username()
		
greet_user()
