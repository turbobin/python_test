# -*- coding: utf-8 -*-
from random import randint

class Die():
	def __init__(self,sides=6):
		"""初始化"""
		self.sides = sides
		
	def roll_die(self):
		x = randint(1,self.sides)
		print (x)
		
die = Die(10)
i = 0
while i < 10:
	die.roll_die()
	i += 1


