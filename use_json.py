#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
from email.policy import default
__author__ = 'caochaobin'
#Created on 2018年5月9日

import json
#序列化一个对象:default
class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        
s = Student('Bob',22,87)

# print(json.dumps(s))    TypeError: Object of type 'Student' is not JSON serializable
print(json.dumps(s,default=lambda obj:obj.__dict__))    
#通常class都有一个__dict__属性，他就是一个dict，用来存储实例变量

# 反序列化:object_hook
json_str = '{"name": "Bob", "age": 22, "score": 87}'
print(json.loads(json_str,object_hook=lambda obj:obj))
        