import logging


def test_log(name='mylog',file_name='log.log',level='DEBUG',sh_level='DEBUG',fh_level='DEBUG'):
    # 一、创建日志收集器
    shouji = logging.getLogger(name)
    # 设置等级
    shouji.setLevel(level)
    # 二、创建日志输出渠道==>控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    shouji.addHandler(sh)
    # 创建日志输出渠道==》文件
    fh = logging.FileHandler(file_name, encoding='utf-8')
    fh.setLevel(fh_level)
    shouji.addHandler(fh)
    #设置日志输出格式
    formatter=logging.Formatter('%(asctime)s--(message)s--%(module)s--%(pathname)s--%(relativeCreated)d')
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #返回一个日志收集器
    return shouji


#为了避免程序中创建多个日志收集器而导致日志重复记录
#那么我们可以只创建一个日志收集器，别的模块的使用时都导入这个日志收集器
#
# log=test_log(
#     name=config.get("logging", 'name'),
#     file_name=log.get("logging","file_name"),
#     level=log.get("logging","level"),
#     sh_level=log.get("logging","sh_level"),
#     fh_level=log.get("logging","fh_level")
# )