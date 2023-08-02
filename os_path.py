import os

# 获取文件的绝对路径
# file_path=os.path.abspath("conf.ini")
# print(file_path)
#
# p1_path=os.path.dirname("conf.ini")
# print(p1_path)

# 魔法变量：变量的值在不同情况下是不一样的
# __name__:
# __file__:
res=os.path.abspath(__file__)
print(res)

res1=os.path.dirname(res)
print(res1)



#获取用例数据文件夹所在目录的绝对路径
data_dir=os.path.join(res1,"datas")
print(data_dir)


