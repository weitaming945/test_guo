# 登录接口
"""
https://fosun.external.yuemia.com/login
post
{username: "yangxiaowu", password: "wer"}
"""
import requests

url = "https://fosun.external.yuemia.com/login"
params = {'username': "yangxiaowu", 'password': "wer"}
# data专门用来传递表单类型的参数
response = requests.post(url=url, data=params)
# post请求
print(response.text)
# get请求
requests.get()

# 常用的请求类型，requests中都封装了请求方法，直接使用requests去调用就可以了
# 请求参数传递的类型
# ========================参数类型是application/json======================================
# 请求地址==》post请求
url = "https://fosun.external.yuemia.com/login"
# 请求头==》接口文档有时候会描述请求头必须添加,以字典的形式
head={'Content-Type':'application/json;charset=UTF-8'}
# 请求参数
parms = {'username': "yangxiaowu", 'password': "wer"}
#发送请求之后请求头使用headers
#参数类型是json的情况下，使用json来传递参数
response = requests.post(url=url, headers=head,json=parms)
print(response.text)
#=============================get请求的参数：查询字符串参数===================
#方式一、查询字符串参数，可以直接拼接在url上
# 接口地址后面使用？拼接参数，参数=参数值，如果多个参数使用&符进行拼接
"""https://fosun.external.yuemia.com/system/dict/data/list?status=0&dictType=material_type"""
url="https://fosun.external.yuemia.com/system/dict/data/list?status=0&dictType=material_type"
#方式二、使用parms进行传递
url="https://fosun.external.yuemia.com/system/dict/data/list"
parmas={"status":0,'dictType':'material_type'}
head={'Content-Type':'application/json;charset=UTF-8'}
response=requests.get(url=url,params=parmas,headers=head)
print(response.text)
#=============================参数类型：form-data===================================
#上传文件时使用files来传递参数
files={}
requests.post(url=url,files=files)