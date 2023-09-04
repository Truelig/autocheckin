import json

import requests

print(666)

pushplush_token = '7b9d76c0804a43fb95d269a0281c42e0'
body = {
    "token": pushplush_token,
    "title": "掘金签到通知",
    "content": '测试数据666',
    "template": "txt"
}
requests.post('http://www.pushplus.plus/send', data=json.dumps(body))
