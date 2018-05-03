# -*- coding: utf-8 -*-
name_map = {
	"张三":19,
	"李四":15,
	"王五":17,
	"赵六":17,
	"朱七":15,
	}
# ~ 遍历字典
for name,age in name_map.items():
	print ("\nname:"+name)
	print ("age:"+str(age))
	
# ~ 遍历所有的键
for name in name_map.keys():	# keys()方法可以省略
	print ("\nname:"+name)

# ~ 遍历所有的值
for age in sorted(name_map.values()):	#排序
	print ("\nage:"+str(age))

# ~ 去除重复的值
for age in set(name_map.values()):
	print (age)

# ~ 嵌套
users = []
for user_num in range(1,5):
	new_users = {"user1":23,"user2":31,"user4":25,"user3":33}
	users.append(new_users)
	
for user in users:
	print (user)
