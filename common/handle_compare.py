#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/9/9 11:21
# @Author : qiaoqiao
# @File : handle_compare.py
# @Software: PyCharm
# @python version: 3.7

from common.handler_log import my_log



# dict_a被包含于dict_b，只能查出a相较于B的不同
def dict_compared(dict_a ,dict_b):
    for key in dict_a.keys():
        print(key)
        if key in dict_b.keys():
            if dict_a[key] is dict_b[key]:
                pass
            else:
                my_log.error("【{}】的value值不同，分别是{}和{}".format(key,dict_a[key],dict_b[key]))

        else:
            my_log.info("{}】没在B字典里面".format(key))





#
# if __name__ == '__main__':
#
#     AandBCompared = AandBCompared()
#     first_dict = {"name":"鸣人","age":22,"sex":"男","title":"六代火影","heigh":"179cm","aaa":0}
#
#     second_dict = {"name":"鸣人","age":22,"sex":"女","title":"六代火影","heigh":"1790cm","bbb":5645}
#
#     AandBCompared.dict_compared(first_dict,second_dict)
