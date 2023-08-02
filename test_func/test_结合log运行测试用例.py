import unittest
from unittestreport import ddt, list_data
from test_func.test_excel_fengzhuang import HandleExcel
from test_func.login_func import login_check
from test_func.log_conf import test_log



@ddt
class TestCase(unittest.TestCase):
    excel = HandleExcel(r'C:\Users\yuemia\PycharmProjects\test_guo\datas\新建 XLSX 工作表.xlsx', 'Sheet1')
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
            # 调用封装的excel写入方法，在excel中回显测试结果,
            self.excel.data_write(row=row, column=5, value='NO')
            test_log().error("用例--【{}】--执行未通过".format(item['title']))
            raise e
        else:
            self.excel.data_write(row=row, column=5, value='Yes')
            test_log().info("用例--【{}】--执行已通过".format(item['title']))
