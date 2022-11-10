"""
数据层的处理
先存入到文件
"""
import os
import json
from config import setting


# 保存用户
def save(user):
    with open(os.path.join(setting.USER_CACHE_DIR, f"{user.get('user_name')}.json"), mode='wt', encoding='utf-8') as f:
        json.dump(user, f)


# 根据用户名查询用户
def query(user_name):
    user_path = os.path.join(setting.USER_CACHE_DIR, f"{user_name}.json")
    if os.path.exists(user_path) and os.path.isfile(user_path):
        with open(user_path,mode='rt',encoding='utf-8') as f:
            user = json.load(f)
            return user
    else:
        return None
