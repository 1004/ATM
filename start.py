"""
ATM 模拟入口执行文件

"""
import os
import sys
from core import src

sys.path.append(os.path.dirname(__file__))  # 如果是在根目录，可加，可不加
# print(os.path.dirname(__file__))
# print(os.path.dirname(__file__))

if __name__ == '__main__':
    src.run()
