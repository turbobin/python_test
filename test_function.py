# -*- coding: utf-8 -*-
# ~ 自动化测试 --测试方法
import unittest
from method_demo import get_name
from method_demo import build_person

class NameTestCase(unittest.TestCase):
	"""测试methon_demo.py"""
	def test_get_name(self):
		full_name = get_name("wanrren")
		self.assertEqual(full_name,"Wanrren ") #断言方法，将结果与期望的结果比较
	
	def test_get_name_full(self):	#命名必须以test_开头，否则不会自动运行
		full_name = get_name("wanrren","cao")	
		self.assertEqual(full_name,"Wanrren Cao")
		
	def test_build_person(self):
		person_info = build_person("wanrren","cao",25)
		values = []
		for key,value in person_info.items():
			values.append(value)
			
		self.assertIn(25,values)
		
print ("\n---------单元测试-----------")			
unittest.main() #自动运行所有以test_开头的方法
