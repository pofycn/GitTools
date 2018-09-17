# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import logging
import os


# 清空日志
def clear_log_content():
    os.remove('logs/GitTools.log')


# 获取Logger
def get_logger():
    return logger


# 读取当前日志信息
def read_logs():
    try:
        file = open('logs/GitTools.log', 'r')
        stdout = file.read()
        return stdout
    except Exception as e:
        print('读取日志文件内容错误:', e)
    finally:
        if file:
            file.close()


logger = logging.getLogger('GitTools_log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/GitTools.log')
fh.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

# set formatter
formatter = logging.Formatter('%(asctime)s:%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# add handler to logger
logger.addHandler(fh)
logger.addHandler(sh)