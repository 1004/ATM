"""
用户交互层
"""

from interface import user_presenter
from lib import common

user = None


# 注册
def register():
    print("欢迎来到注册页面:")
    while True:
        user_name = input("请输入名称：").strip()
        user_pwd = input("请输入密码：").strip()
        repeat_pwd = input("请确认密码：").strip()
        if len(user_name) == 0 or len(user_pwd) == 0 or len(repeat_pwd) == 0:
            print("输入内容不能为空,请重新输入")
            continue
        if user_pwd != repeat_pwd:
            print("重试密码和确认密码不正确")
            continue
        result, msg = user_presenter.register(user_name, user_pwd)
        if result:
            print("注册成功")
            break
        else:
            print(f"注册失败:{msg}，继续注册")
            continue

    print("返回首页了")


# 登录
def login():
    print("欢迎来到登录页面:")
    while True:
        user_name = input("请输入名称：").strip()
        user_pwd = input("请输入密码：").strip()
        if len(user_name) == 0 or len(user_pwd) == 0:
            print("输入内容不能为空,请重新输入")
            continue
        result, obj = user_presenter.login(user_name, user_pwd)
        if result:
            print(f"登录成功,欢迎{obj.get('user_name')}")
            global user  # 必须使用全局的
            user = obj
            break
        else:
            print(f"登录失败:{obj},重新登录")
            continue
    print("返回首页了")


# 查看余额
@common.login_auth
def check_balance():
    if user:
        print(f"你的余额：{user.get('balance')}")


# 充值
@common.login_auth
def recharge_money():
    print("欢迎来到充值页面:")
    while True:
        money_str = input("请输入充值金额：").strip()
        if len(money_str) == 0 or not money_str.isdigit():
            print("充值金额输入有问题，请重新输入")
            continue
        result, obj = user_presenter.recharge(user.get('user_name'), int(money_str))
        if result:
            print("充值成功")
            user['balance'] = obj['balance']
            break
        else:
            print(f"充值失败：{obj}，请重新输入")
            continue
    print("返回首页了")


# 购物
@common.login_auth
def shopping():
    pass


dict_fun = {
    "1": ["注册", register],
    "2": ["登录", login],
    "3": ["查看余额", check_balance],
    "4": ["充值", recharge_money],
    "5": ["购物", shopping],
}


#  入口函数
def run():
    while True:
        print("======命令介绍=======")
        print("0:退出系统")
        for k in dict_fun:
            print(f"{k}:{dict_fun.get(k)[0]}")

        print("======命令介绍=======")

        code = input("请输入指令：").strip()
        if code not in dict_fun:
            if code == "0":
                print("退出系统了")
                break
            else:
                continue
        dict_fun.get(code)[1]()
