#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a python_test demo'
__author__ = 'caochaobin'
#Created on 2018年5月12日

from email.mime.text import MIMEText
# from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
msg = MIMEText('hello, this is a test-mail...', 'plain', 'utf-8')
# 第一个参数是邮件正文，第二个第二个参数是MIME的subtype，
# 传入'plain'表示纯文本，最终的MIME就是'text/plain'

# 输入Email地址和口令:
from_addr = 'cao.chb@vivebest.com'
# from_addr = 'xeus155225@163.com'
# from_addr = '2444343677@qq.com'
password = 'ccb151517'
# 输入收件人地址:
to_addr = '1571616014@qq.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    # 如果有中文，需要通过Heardr对象进行编码

msg['From'] = _format_addr('turbobin <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('test', 'utf-8').encode()

# 输入SMTP服务器地址:
# smtp_server = 'smtp.qq.com'
smtp_server = 'mail.vivebest.com'

import smtplib
try:
#     server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
#     server = smtplib.SMTP(smtp_server, 587) # 使用starttls加密传输
#     server.starttls()
    server = smtplib.SMTP_SSL(smtp_server, 465) # 使用SSL加密传输
    server.set_debuglevel(1)    #打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('send succeed!')
except smtplib.SMTPException:  
    print('send error.')
    