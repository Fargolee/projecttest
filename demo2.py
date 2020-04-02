import requests
from requeststools import request


url = "http://192.144.148.91:2333/login"
data = {"username":"liuyun1", "password":"a12345678"}
method = 'post'
headers = {"Content-Type":"application/json"}
res = requests.request(method, url=url, json=data, headers=headers)
print(res.text)

url = "http://192.144.148.91:2333/get_title_img"
res = requests.request('get', url=url)
print(res.text)

r = request('get', url)
print(r)
