import unittest
from test_func.login_func import login_check


class TestCase(unittest.TestCase):
    def test_username_None(self):
        '用户名为空'
        parms = {'username': None, 'password': 'test'}
        excepted = {'code': 1, 'msg': '账号或密码不能为空'}
        # 调用功能函数，获取实际结果
        res = login_check(**parms)
        # 断言
        self.assertEqual(excepted, res)