#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/6/15 14:26
# @Author : qiaoqiao
# @File : handle_path.py
# @Software: PyCharm
# @python version: 3.7

'''此模块专门用来处理项目中的绝对路径'''

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)

# 用例数据所在目录
DATA_DIR = os.path.join(BASE_DIR,'data')
# print(DATA_DIR)

# 配置文件所在目录
CONF_DIR = os.path.join(BASE_DIR,'conf')

# 日志所在目录
LOG_DIR = os.path.join(BASE_DIR,'logs')
# print(LOG_DIR)

# 报告所在目录
REPORT_DIR = os.path.join(BASE_DIR,'reports')

# 用例模块所在目录
CASES_DIR = os.path.join(BASE_DIR,'testcases')

# 数据样例文件所在目录
DATA_SAMPLE = os.path.join(BASE_DIR,'datasample')