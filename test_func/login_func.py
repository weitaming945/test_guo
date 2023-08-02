def login_check(username=None, password=None):
    if username != None and password != None:
        if username == 'python' and password == 'test':
            return {'code': 0, 'msg': '登录成功'}
        else:
            return {'code': 1, 'msg': '账号或者密码不正确'}
    else:
        return {'code': 1, 'msg': '账号或密码不能为空'}
