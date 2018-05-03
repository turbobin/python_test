# -*- coding: utf-8 -*-
cars = ["bmw","audi","subaru","toyota"]
for car in cars:
	if car == "bmw":
		print (car.upper())
	else:
		print (car.title())
	

if "BYD" not in cars:
	cars.append("byd")
	print (cars)

# ~ if-elif-else 结构
age = 19
if age < 4:
	price = 0
elif age <18:
	price = 5
elif age < 20:
	price = 8
else:
	price = 10
print ("your price is: "+str(price))


# Tips:
name = []
if name:	#当列表不为空时返回True
	print (name)
else:
	print ("null...")

