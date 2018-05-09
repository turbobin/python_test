# -*- coding: utf-8 -*-
# ~ 自动化测试 --测试类
import unittest
from class_demo import Car

class TestCar(unittest.TestCase):
	"""针对类的测试"""
	def setUp(self):		#此方法最先运行，将会在调用方法的每一次开始前执行
		print('setUp...')
		self.my_car = Car('BYD','SS5',2018)	#创建一个类的实例
		
	def test_get_desc_name(self):
		decs = self.my_car.get_desc_name()
		self.assertEqual(decs,"2018 BYD SS5")
		
		
	def test_miles(self):
		self.my_car.miles = 10
		self.my_car.add_miles(150)
		miles = self.my_car.read_miles()
		self.assertEqual(miles,160)
		
	def tearDown(self):	#将会在每一次调用方法的后面执行
		print('tearDown....')

print ("\n---------单元测试-----------")	
unittest.main()
		
#若期待输出结果与指定的相等，使用assertEqual
#若期待抛出指定类型异常，使用assertRaises
#若期待指定的布尔值，使用assertTrue/使用assertFalse
#若期待元素在指定的列表中，使用assertIn
