#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spidemovie.py
#  
#  Copyright 2018 Administrator <Administrator@CCB>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests
from pyquery import PyQuery as pq

#обть
r = requests.get("https://movie.douban.com/top250");

file_name = "C:/Users/Administrator/Desktop/douban.txt"
with open(file_name,'w') as file_object:
	for item in pq(r.content)('.item'):
		title = pq(item).find('.title').html()
		desc = pq(item).find('.inq').html()
		print (title,"/",desc)
		file_object.write(title+" / "+desc+"\n")
