
def describe_pet(pet_name,animal_type="dog"):	#可预先指定默认值
	"""显示宠物信息"""	#文档注释
	print ("\nI hava a "+animal_type.title())
	print ("His name is "+pet_name)
	
describe_pet("harry","dog")
describe_pet("harry")
describe_pet("harry",animal_type="cat")	#将覆盖默认值

def get_name(first_name,last_name=""):
	"""返回一个整洁的名字"""
	full_name = first_name+" "+last_name
	return full_name.title()
	
name = get_name("jimi","hendrix")
print ("\n"+name)
name = get_name("tomcat")
print ("\n"+name)


def build_person(first_name,last_name,age):
	"""返回一个字典，其中包含一个人的相关信息"""
	person = {'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
	
musician = build_person("jimi","hendrix",age=27)
print ("\n"+str(musician))


