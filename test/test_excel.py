import unittest
from unittestreport import ddt, list_data
from test_func.test_excel_fengzhuang import HandleExcel
from test_func.login_func import login_check
from test_func.login_register import login_register
import os
from conf.handle_path import data_dir

@ddt
class TestCase(unittest.TestCase):
    excel = HandleExcel(r'/datas/新建 XLSX 工作表.xlsx', 'Sheet1')
    cases = excel.read_data()

    @list_data(cases)
    def test_login_excel(self, item):
        parms = eval(item['data'])
        excepted = eval(item['excepted'])
        # 获取要回显的行号
        row = item['id'] + 1
        res = login_check(**parms)
        # 在excel中回显测试结果
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('用例执行未通过')
            # 调用封装的excel写入方法，在excel中回显测试结果,
            self.excel.data_write(row=row, column=4, value='NO')
            raise e
        else:
            print("用例执行已通过")
            self.excel.data_write(row=row, column=4, value='Yes')


@ddt
class TestCase_1(unittest.TestCase):
    excel = HandleExcel(r'/datas/新建 XLSX 工作表.xlsx', 'Sheet2')
    cases = excel.read_data()

    @list_data(cases)
    def test_register(self, item):
        parms = eval(item['data'])
        excepted = eval(item['excepted'])
        row = item['id'] + 1
        res = login_register(**parms)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('注册用例执行未通过')
            self.excel.data_write(row=row, column=4, value='no')
            raise e
        else:
            print('注册用例执行通过')
            self.excel.data_write(row=row, column=4, value='yes')
