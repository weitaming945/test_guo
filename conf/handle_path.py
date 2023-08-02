"""此模块是专门处理项目中的绝对路径"""
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#测试用例的路径
data_dir=os.path.join(base_dir,"datas")
#获取配置文件的路径
conf_dir=os.path.join(base_dir,"conf")
#获取报告文件的路径
report_dir=os.path.join(base_dir,"report")
#获取日志文件的路径
log_dir=os.path.join(base_dir,"log")
#获取用例模块文件的路径
testcase_dir=os.path.join(base_dir,"test_func")