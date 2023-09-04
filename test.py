import json
import os
import requests

print(666)
envs = dict(os.environ)
pushplush_token = envs['pushplush_token']
body = {
    "token": pushplush_token,
    "title": "掘金签到通知",
    "content": '测试数据999',
    "template": "txt"
}
requests.post('http://www.pushplus.plus/send', data=json.dumps(body))
