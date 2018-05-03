# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq

#下载
r = requests.get("https://movie.douban.com/top250");

file_name = "C:/Users/Administrator/Desktop/douban.txt"
with open(file_name,'w') as file_object:
    for item in pq(r.content)('.item'):
        title = pq(item).find('.title').html()
        desc = pq(item).find('.inq').html()
        print (title,"/",desc)
        file_object.write(title+" / "+desc+"\n")
