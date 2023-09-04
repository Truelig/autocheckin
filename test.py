import json
import os
import requests

envs = dict(os.environ)
pushplush_token = envs['pushplush_token']
juejin_cookie = envs['juejin_cookie']

url = "https://api.juejin.cn/growth_api/v1/check_in"
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Cookie": juejin_cookie
}
data = "签到失败"
response = requests.post(url, headers=headers)
responseJson = response.json()
if ('success' == responseJson['err_msg']):
    data = "总积分" + responseJson['sum_point'] + "," + "增长" + responseJson['incr_point']
else:
    data = responseJson['err_msg']
body = {
    "token": pushplush_token,
    "title": "掘金签到通知g",
    "content": data,
    "template": "txt"
}
requests.post('http://www.pushplus.plus/send', data=json.dumps(body))
