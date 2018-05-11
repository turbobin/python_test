#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月11日
import hashlib

user_dict = {}
def store_info(name,password):
    msk_psw = mask_psw(name,password)
#     print('name    ','\tpassword')
#     print(name,msk_psw)
    user_dict[name] = msk_psw
    
def login(name,password):
    msk_psw = mask_psw(name,password)
    if user_dict[name] == msk_psw:
        print('logon succeed!')
    else:
        print('name or password error!')

# MD5：最常见的摘要算法，另一种是SHA1,用法和MD5一致
def mask_psw(name,password): #对密码做MD5算法加密处理
    md5 = hashlib.md5()
    md5.update((password+name+'the-salt').encode('utf-8'))  #加盐处理
    msk_psw = md5.hexdigest()
    return msk_psw

store_info('caocb.sdc','ccb5431263')
store_info('turbin','turbin123')
store_info('root','root')
print(user_dict)

login('caocb.sdc','ccb5431263')
login('root','rrot')
