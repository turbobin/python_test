#!/usr/bin/env python
# -*- coding: utf-8 -*-

name_map = {"张三":14,"李四":15,"王五":17}
# 查询
print (name_map["李四"])

# ~ 添加键值对
name_map["赵六"] = 20
name_map["朱七"] = 22
print (name_map)

# ~ 修改
name_map["李四"] = 18
print (name_map)

# ~ 删除
del name_map["王五"]
print ("\n"+str(name_map))




