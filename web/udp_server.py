#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月11日
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SOCK_DGRAM指定了这个Socket的类型是UDP
# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，
# 直接调用sendto()就可以把数据用UDP发给客户端