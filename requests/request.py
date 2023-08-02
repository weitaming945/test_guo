import requests
# --------------------------------------------------------------------------------------------------------------------
#发送一个请求
url="https://fosun.external.yuemia.com/web/login-manual"
respones=requests.get(url=url)
#获取返回的响应状态码
print(respones.status_code)
#获取响应头
print(respones.headers)
#获取响应体
#方法1：对于返回任意类型的数据都可使用这个方法进行获取==》自动识别返回内容的编码，进行解码（可能会乱码）
print(respones.text)
#方法2：可以手动指定编码进行解码
print(respones.content.decode("utf-8"))
#方式3：只能在返回数据是json的情况下使用==》接口测试常用
print(respones.json())
# --------------------------------------------------------------------------------------------------------------------
#1.获取请求头
print(respones.request.headers)
#获取请求体
print(respones.request.body)
#---------------------------------------------------------------------------------------------------------------------