#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月13日

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])    #通过装饰器在内部自动地把URL和函数给关联起来
def home():     # get /:首页，返回home
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():  #GET /signin：登录页，显示登录表单；
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():   #POST /signin：处理登录表单，显示登录结果
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()   #运行，Flask自带的Server在端口5000上监听：