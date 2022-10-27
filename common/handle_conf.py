#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/30 16:34
# @Author : qiaoqiao
# @File : handle_conf.py
# @Software: PyCharm
# @python version: 3.7

import os
from configparser import ConfigParser
from S_接口耗时检测.common.handle_path import CONF_DIR


class Config(ConfigParser):
    '''在创建对象时直接加载配置文件中的内容'''

    def __init__(self, conf_file):
        super().__init__()  # 为了保证父类的原有功能正常，要调用一下原父类的方法
        self.read(conf_file, encoding='UTF-8')


conf = Config(os.path.join(CONF_DIR,'config.ini'))
# print(os.path.join(CONF_DIR,'config.ini'))

# if __name__=='__main__':
# conf = ConfigParser()
# conf.read(r'D:\tungee文件\newstart\ningmengban\day2022_0525\config.ini',encoding = 'UTF-8')  # 加载一下配置文件的数据

# conf = Config(r'D:\tungee文件\newstart\ningmengban\day2022_0525\config.ini')
# name = conf.get('logging', 'name')
# level = conf.get('logging', 'level')
# filename = conf.get('logging', 'filename')
# sh_level = conf.get('logging', 'sh_level')
# fh_level = conf.get('logging', 'fh_level')

# print(name)
# print(level)
# print(filename)
# print(sh_level)
# print(fh_level)
