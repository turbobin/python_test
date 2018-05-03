# -*- coding: utf-8 -*-
#
#  methon_test.py

#传递列表
def print_eles(unprint_eles,printed_eles):
	"""
	打印每个元素，直到全部打印，每打印一个，将其移到已打印列表中
	"""
	while unprint_eles:
		current_ele = unprint_eles.pop()
		print ("Printing ele:"+current_ele)
		printed_eles.append(current_ele)

unprint_eles = ["a3","a2","a5","a1"]
printed_eles = []
print_eles(unprint_eles,printed_eles)
# ~ print_eles(unprint_eles[:],printed_eles)	#unprint_eles将不会被修改

print("unprint_eles[]="+str(unprint_eles))	
print("printed_eles[]="+str(printed_eles))	

# ~ 传递任意数量实参
def make_pizza(size,*toppings):
	"""说明要制作的披萨"""
	
	if not isinstance(size, (str,int)):	#对传入的参数做检查
		raise TypeError("bad oprand type,not int or str")
		
	print ("\nMaking a "+str(size)+
			"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
		
make_pizza('16.3',"pepperoni")
make_pizza(13,"mushroom","green peppers","extra cheese")
pizza_typ = ["mushroom","green peppers","extra cheese"]
make_pizza(14,*pizza_typ)	# *pizza_typ表示把这个list所有元素作为可变参数传递进去

# ~ 使用任意数量的关键字参数
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert','einstein',
							location='princeton',
							filed='physics')
							#传参时，等号两边最好不要有空格

print(user_profile)
