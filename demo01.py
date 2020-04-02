import requests

# 1、登录
url = "http://192.144.148.91:2333/login"
data = {"username": "lisi111","password": "a1234567"}
res = requests.post(url=url,json=data)
assert res.status_code == 200  #如果断言通过，就继续往下执行，反之报错
assert res.json()['status'] == 200
token = res.json()['data']['token']  
print("登录成功！")
#2、写文章
url = "http://192.144.148.91:2333/article/new"
data = {
"title":"为什么要学习测试",
"content":"内容", 
"tags":"测试", 
"brief":"介绍", 
"ximg":"dsfsdf.jpg" 
}
headers = {"token":token}
res = requests.post(url=url,json=data,headers=headers)
assert res.status_code == 200  
assert res.json()['status'] == 200
aid = res.json()['data']['articleid']
print("写文章成功！")
#3、修改文章
url = "http://192.144.148.91:2333/article/update"
data = {
"title":"学习测试",
"content":"内容", 
"tags":"测试", 
"brief":"介绍", 
"ximg":"dsfsdf.jpg",
'aid':aid
}
headers = {"token":token}
res = requests.post(url=url,json=data,headers=headers)
assert res.status_code == 200  
assert res.json()['status'] == 200
print('修改文章成功！')


#   
# if res.status_code ==200:
#     if res.json()['status'] == 200:
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print(res.status_code)
#     print("状态码错误")

#判断http状态码
# if res.status_code ==200:
#     print("状态码正常")
# else:
#     print("状态码错误")
# #判断登录成功
# if res.json()['status'] == 200:
#     print("登录成功")
# else:
#     print("登录失败")

# token = res.json()['data']['token']  #.json()将结果转换为字典

#2、写文章

#3、修改文章