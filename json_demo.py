# -*- coding: utf-8 -*-
import json

numbers = [1,3,5,2,7,11]
filename = 'number.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)


with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print (numbers)
