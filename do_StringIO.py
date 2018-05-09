#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月9日

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO #在内存中读写str

# write to StringIO:
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue()) #getvalue()方法用于获得写入后的str

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())