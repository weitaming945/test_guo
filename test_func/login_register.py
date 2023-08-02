"""注册功能函数
user：guo，phone：13087070301，password：123456
{'code':0,'msg':'注册成功'}
"""


def login_register(user=None, phone=None, password=None):
    if user != None and phone != None and password != None:
        if user == 'guo' and phone == '13087070301' and password == '123456':
            return {'code': 0, 'msg': '注册成功'}
        else:
            return {'code': 1, 'msg': '注册失败'}
    else:
        return {'code': 1, 'msg': '必填字段不能为空'}
