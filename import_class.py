# -*- coding: utf-8 -*-
from class_demo import Car	#导入类

class ChinaCar(Car):
	"""继承，描述子类的特有属性"""
	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)
		self.country = "China"
		self.chinacar_size = Size()
		
	# ~ 给子类定义属性和方法
	def car_made(self):
		print ("made in "+self.country)
	
class Size():
	def __init__(self,size=70):
		"""初始化"""
		self.car_size = size
		
	def describe_size(self):
		print ("this car has "+str(self.car_size)+" size")
			
my_byd = ChinaCar("BYD","B7",2016)
print (my_byd.get_desc_name())

my_byd.car_made()
my_byd.chinacar_size.describe_size()
