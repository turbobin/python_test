#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月11日
from PIL import Image,ImageFilter

#打开一个图像文件
im = Image.open(r'C:\Users\hmx\Desktop\me.jpg')
#获得图像尺寸
w, h = im.size
print('图片尺寸:(%s,%s)' %(w,h))

#缩放到50%
im.thumbnail((w//2,h//2))
#把缩放后的图像用jpeg格式保存
im.save(r'C:\Users\hmx\Desktop\minime.jpg','jpeg')
print('缩略图已保存')

#模糊
im = im.filter(ImageFilter.BLUR)
im.save(r'C:\Users\hmx\Desktop\caverme.jpg','jpeg')