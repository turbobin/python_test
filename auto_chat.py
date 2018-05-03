# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):     
    url = "http://www.tuling123.com/openapi/api"
    api_key = "46a3443d543441ee882c8c7aaac681cb"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "238177"
    }
    r = requests.post(url, data=json.dumps(payload))     
    result = json.loads(r.content)     
    return "[图灵机器人] " + result["text"]

bot = Bot(console_qr=False, cache_path=True)

my_friend = bot.friends().search('如暘', sex=MALE, city="深圳")[0]
print (my_friend)
@bot.register(my_friend)
def forward_message(msg):     
    return auto_reply(msg.text)

embed()
