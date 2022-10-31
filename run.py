#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/10/28 18:03
# @Author : qiaoqiao
# @File : run.py
# @Software: PyCharm
# @python version: 3.7


import unittest
from unittestreport import TestRunner
from common.handle_path import  CASES_DIR,REPORT_DIR

suit = unittest.defaultTestLoader.discover(CASES_DIR)

runner = TestRunner(suit,
                    filename="report.html",
                    report_dir=REPORT_DIR,)

runner.run()