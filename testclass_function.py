# -*- coding: utf-8 -*-
# ~ 自动化测试 --测试类
import unittest
from class_demo import Car

class TestCar(unittest.TestCase):
	"""针对类的测试"""
	def setUp(self):		#此方法最先运行
		self.my_car = Car('BYD','SS5',2018)	#创建一个类的实例
		
	def test_get_desc_name(self):
		decs = self.my_car.get_desc_name()
		self.assertEqual(decs,"2018 BYD SS5")
		
	def test_miles(self):
		self.my_car.miles = 10
		self.my_car.add_miles(150)
		miles = self.my_car.read_miles()
		self.assertEqual(miles,160)

print ("\n---------单元测试-----------")	
unittest.main()
		
