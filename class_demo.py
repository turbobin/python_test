# -*- coding: utf-8 -*-
class Car():
	"""描述汽车"""
	def __init__(self,make,model,year):	#构造函数前后两个下划线
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.miles = 0
		# ~ print (self)	#打印的是对象属性
		
	def get_desc_name(self):
		"""返回整洁的描述信息"""
		long_time = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_time
		
	def read_miles(self):
		"""打印一条消息输出汽车里程"""
		print ('\nThis car has '+str(self.miles)+' on it')
		return self.miles
		
	def add_miles(self,meters):
		"""增加里程"""
		self.miles += meters
		
my_car = Car('BMW','S5',2017)	#创建一个类的实例
print (my_car.get_desc_name())

my_car.miles = 30
my_car.add_miles(100)	
my_car.read_miles()
