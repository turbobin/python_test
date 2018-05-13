#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月12日

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'cao.chb@vivebest.com'
password = 'ccb151517'
receivers = ['1571616014@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("caocb.sdc <%s>" %sender, 'utf-8')
msgRoot['To'] =  Header('管理员 <%s>' % receivers[0], 'utf-8')
subject = 'Python SMTP 邮件测试 '
msgRoot['Subject'] = Header(subject, 'utf-8')
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

 
mail_msg = """
<p>Python 邮件发送测试  - 添加图片...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
# 指定图片
fp = open(r'C:\Users\Administrator\Desktop\me.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp_server = 'mail.vivebest.com'
try:
    smtpObj = smtplib.SMTP(smtp_server, 25)
    smtpObj.set_debuglevel(1)
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error: 无法发送邮件")