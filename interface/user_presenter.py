"""
用户逻辑层
"""

from db import db_user
from lib import common


def register(user_name, user_pwd):
    old_user = db_user.query(user_name)
    if old_user:
        return False, "注册失败，用户名已经存在"
    user = {
        "user_name": user_name,
        "user_pwd": common.get_md5_pwd(user_pwd),
        "balance": 0,
        "lock": False
    }
    db_user.save(user)
    return True, "注册成功"


def login(user_name, user_pwd):
    old_user = db_user.query(user_name)
    if old_user:
        pwd = common.get_md5_pwd(user_pwd)
        if pwd == old_user.get('user_pwd'):
            return True, old_user
        else:
            return False, "密码错误"

    else:
        return False, "用户未注册"


# 充值
def recharge(user_name, money):
    if money < 0:
        return False, "钱数有问题"
    old_user = db_user.query(user_name)
    if old_user:
        oldmoney = old_user.get('balance')
        newmoney = oldmoney + money
        old_user['balance'] = newmoney
        db_user.save(old_user)
        return True, old_user
    else:
        return False, "用户未注册"
