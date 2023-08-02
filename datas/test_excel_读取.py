import openpyxl
import unittest
from unittestreport import ddt, list_data
from test_func.login_func import login_check

# 创建工作簿
workbook = openpyxl.load_workbook(r'C:\Users\yuemia\PycharmProjects\test_guo\datas\新建 XLSX 工作表.xlsx')
# 选中表单
sheet = workbook['Sheet1']
# 选中行数
row = list(sheet.rows)
# 获取第一行的数据
title = [i.value for i in row[0]]
cases = []
# 获取除一行以外的数据
for item in row[1:]:
    data = [i.value for i in item]
 # 将title与data进行字典打包
    dic = dict(zip(title, data))
    cases.append(dic)


# 将获取到数据加载到测试用例中执行结果

@ddt
class TsetCase_1(unittest.TestCase):
    @list_data(cases)
    def test_login_check_excel(self, item):
        parms = eval(item['data'])
        excepted = eval(item['excepted'])
        res = login_check(**parms)
        self.assertEqual(excepted, res)
