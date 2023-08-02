import unittest
from test_func.login_func import login_check
from test_func.login_register import login_register


class TestCase(unittest.TestCase):
    def test_ok(self):
        "登录成功"
        parms = {'username': 'python', 'password': 'test'}
        excepted = {'code': 0, 'msg': '账号登录成功'}
        # 调用功能函数，获取实际结果
        res = login_check(**parms)
        # 断言
        self.assertEqual(excepted, res)

    def test_password_error(self):
        "密码错误"
        parms = {'username': 'python', 'password': 'test11'}
        excepted = {'code': 1, 'msg': '账号或者密码不正确'}
        # 调用功能函数，获取实际结果
        res = login_check(**parms)
        # 断言
        self.assertEqual(excepted, res)

    def test_username_error(self):
        '用户名错误'
        parms = {'username': 'python11', 'password': 'test'}
        excepted = {'code': 1, 'msg': '账号或者密码不正确'}
        # 调用功能函数，获取实际结果
        res = login_check(**parms)
        # 断言
        self.assertEqual(excepted, res)


    def test_register_1(self):
        params={'user':'guo','phone':'13087070301','password':'123456'}
        excepted={'code': 0, 'msg': '注册成功'}
        res=login_register(**params)
        self.assertEqual(excepted,res)