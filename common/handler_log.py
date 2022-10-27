#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/10 11:56
# @Author : qiaoqiao
# @File : handler_log.py
# @Software: PyCharm
# @python version: 3.7
'''
为了避免程序中创建多个日志收集器而导致的日志重复记录，
那我们只创建一个日志收集器，别的模块引用此日志收集器
'''

import logging
import os
from S_产业数据云2.common.handle_conf import conf
from S_产业数据云2.common.handle_path import LOG_DIR


def create_log(name='mylog.log', level='DEBUG', filename='log.log', sh_level='DEBUG', fh_level='DEBUG'):
    # print('---------------debug------------')
    # print(level)
    # print('-----------debug end------------')
    # 第一步：创建日志收集器
    log = logging.getLogger(name)

    # 第二步：设置日志收集器的等级
    log.setLevel(level)

    # 第三步：设置日志输出渠道
    # 1. 输出到文件的配置
    fh = logging.FileHandler(filename, encoding="UTF-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 2. 输出到控制台的配置
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 第四步：设置日志输出的格式
    formats = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s:%(message)s '
    log_format = logging.Formatter(formats)
    # 第五步： 返回一个日志收集器
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 返回一个日志收集器
    return log


# 解决日志重复输出
my_log = create_log(
    name=conf.get('logging', 'name'),
    level=conf.get('logging', 'level'),
    # filename=LOG_DIR+conf.get('logging', 'filename'),
    filename=os.path.join(LOG_DIR, conf.get('logging', 'filename')),
    sh_level=conf.get('logging', 'sh_level'),
    fh_level=conf.get('logging', 'fh_level')
)
