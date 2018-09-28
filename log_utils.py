# -*- coding: utf-8 -*-

"""
封装日志工具
"""

__author__ = 'Jerry Chan'

import logging
import os

logger = logging.getLogger('GitTools_log')

if (not os.path.exists('logs/GitTools.log')):
    os.makedirs('logs')
    file = open('logs/GitTools.log', 'w')
    file.write('')
    file.close()

logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/GitTools.log')
fh.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

# set formatter
# formatter = logging.Formatter('%(asctime)s:%(message)s')
formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# add handler to logger
logger.addHandler(fh)
logger.addHandler(sh)


# 清空日志内容记录
def clear_log_content():
    with open('logs/GitTools.log', 'r+') as file:
        read_data = file.read()
        file.seek(0)
        file.truncate()


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
