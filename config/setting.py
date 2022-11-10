"""
一些设置
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
USER_CACHE_DIR = os.path.join(BASE_DIR, 'db')

if __name__ == '__main__':
    print(BASE_DIR)
    print(USER_CACHE_DIR)
