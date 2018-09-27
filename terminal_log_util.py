# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import main_window
import log_utils


class TerminalLog():
    def __init__(self, root_window, logger):
        self.root_window = root_window
        self.logger = logger

    # 同时向界面终端及日志文件打印日志信息
    def info(self, message):
        self.logger.info(message)
        self.root_window.append_text_to_text_area(message)
