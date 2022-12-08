#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/9/29 15:17
# @Author : qiaoqiao
# @File : test_handle_requests.py
# @Software: PyCharm
# @python version: 3.7

import json
import os
import requests
import unittest
from unittestreport import ddt,list_data

from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handler_log import my_log

@ddt
class interface_request(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "interface.xlsx"), "Sheet1")
    case = excel.read_data()

    @classmethod
    def setUpClass(cls):
        from common.handel_login import cookies
        cls.Cookie = cookies

    def comm_score_judgment(self,score,row,col):
        print(score)
        if  score< 200:
            # print("A")
            self.excel.write_data(row, col, "A")
        elif 200<=score < 500:
            # print("B")
            self.excel.write_data(row, col, "B")
        elif 500 <= score < 1000:
            # print("C")
            self.excel.write_data(row, col, "C")
        elif 1000 <= score:
            # print("D")
            self.excel.write_data(row, col, "D")

    @list_data(case)
    def test_requests_post(self,item):

        time,code = 0,0

        headers = {
            "Referer": item["host"]+item["api"],
            "Cookie": self.Cookie
        }

        if item["case_id"] == 1 or item["case_id"] == 2 or item["case_id"] == 3:
            self.skipTest('skip')
        else:
            for i in range(3):
                if item["request_mode"] == "post":
                    res = requests.post(item["host"]+item["api"], data=eval(item["data"]), headers=headers)

                    time += res.elapsed.total_seconds()
                    # if res.status_code == 200:
                    #     code = 200
                    # else:
                    #     my_log.error("接口--【{}】第【{}】次执行失败".format(item["title"], i))
                    try:
                        print(res.status_code)
                        print(item["expected"])
                        self.assertEqual(res.status_code,item["expected"])

                    except AssertionError as e:
                        my_log.error("接口--【{}】第【{}】次执行失败".format(item["title"], i))



                elif item["request_mode"] == "get":
                    res = requests.get(item["host"]+item["api"],params=eval(item["data"]), headers=headers)

                    time += res.elapsed.total_seconds()
                    if res.status_code == 200:
                        code = 200
                    else:
                        my_log.error("接口--【{}】第【{}】次执行失败".format(item["title"],i))

            #  将接口状态及返回时间写入文件
            self.excel.write_data(item["case_id"] + 1, 3, code)
            self.excel.write_data(item["case_id"]+1,4,("%.2f"%(time/3)))
            #  打分，并写入文件
            self.comm_score_judgment(time/3*1000,item["case_id"] + 1, 5)





