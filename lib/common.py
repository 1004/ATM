"""
通用工具 能力
"""
import hashlib
from config import setting  # 自己的导入
from logging import config, getLogger  # 内置的日志模块导入


# 密码加密
def get_md5_pwd(row_pwd):
    md5 = hashlib.md5()
    md5.update(row_pwd.encode())
    md5.update("232332".encode())
    return md5.hexdigest()


# 权限验证 ，切面判断

def login_auth(fun):
    def inner(*args, **kwargs):
        from core import src  # 防止循环嵌套  所以局部导入
        if src.user:
            result = fun(*args, **kwargs)
            return result
        else:
            print("未登录，无权限操作，请登录")
            src.login()

    return inner


# 日志功能
def get_logger(log_type):
    config.dictConfig(setting.LOGGING_DIC)  # 设置配置
    return getLogger(log_type)  # 返回log对象
