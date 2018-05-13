#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月12日

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
# 邮件对象:
msg = MIMEMultipart()

# 输入Email地址和口令:
from_addr = 'cao.chb@vivebest.com'
password = 'ccb151517'
to_addr = ['1571616014@qq.com','2444343677@qq.com']
msg['From'] = Header("caocb.sdc <%s>" %from_addr, 'utf-8')
msg['To'] =  Header('管理员 <%s>' % to_addr[0], 'utf-8')
subject = 'Python邮件测试'
msg['Subject'] = Header(subject, 'utf-8')

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(r'C:\Users\Administrator\Desktop\me.png', 'rb') as f:
    #方式一：
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image', 'png', filename='test.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)

    # 方式二:
    # 构造附件1，传送当前目录下的 me.png 文件
    att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.png"'
    msg.attach(att1)
    

# 输入SMTP服务器地址:
# smtp_server = 'smtp.qq.com'
smtp_server = 'mail.vivebest.com'
try:
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
#     server = smtplib.SMTP(smtp_server, 587) # 使用starttls加密传输
#     server.starttls()
#     server.set_debuglevel(1)    #打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('send succeed!')
    server.quit()
except smtplib.SMTPException:
    print('send error.')