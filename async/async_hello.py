#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月14日

import threading
import asyncio

@asyncio.coroutine      #把一个生成器标记为协程类型
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = await asyncio.sleep(1)
#     yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()