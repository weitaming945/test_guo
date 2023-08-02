
import requests
#创建一个回话对象(使用session对象去发生请求，会自动记录请求cookie信息，下一次请求自动添加cookie)
s=requests.sessions()
#登录接口
url = "https://fosun.external.yuemia.com/login"
# 请求头==》接口文档有时候会描述请求头必须添加,以字典的形式
head={'Content-Type':'application/json;charset=UTF-8'}
# 请求参数
parms = {'username': "yangxiaowu", 'password': "wer"}
#发送请求之后请求头使用headers
#参数类型是json的情况下，使用json来传递参数
response = s.post(url=url, headers=head,json=parms)
print(response.text)

#在登录之后才能查看内容==》获取查看列表的接口
url="https://fosun.external.yuemia.com/content/flowListNum"
response=s.get(url=url)
print(response.text)