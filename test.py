# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import re
import log_utils
import arrow
import version_tools_cmft as cmft_tools
import gitlab_tools


def main():
    # log_utils.clear_log_content()

    # arw = arrow.utcnow()
    # next_arw=arw.shift(weekday=3).format('YYYYMMDD')
    # print(next_arw)

    # path1: /Users/pofy/Documents/projects_py/GitTools
    # path2: /Users/pofy/Documents/projects/shop-app
    print('=========================测试=========================')
    # print(cmft_tools.check_branch_exist('master', stdout))
    # print(cmft_tools.get_lastest_branch(stdout))
    
    # current_time = arrow.get("2018-09-21 11:30", "YYYY-MM-DD HH:mm")
    # weekday = current_time.format('ddd')
    # print('当前日期：', current_time, weekday)
    # print('Fri' == weekday)
    # if('Fri'==weekday):
    #     current_time = current_time.shift(days=-1)
    # next_version_date = current_time.shift(weekday=3).shift(weeks=+1).format('YYYYMMDD')
    # print('下期版本日期:' + next_version_date)

    # gitlab_tools.set_access_token('1hPfJmrdmuZMuJAeS1fy')

if __name__ == '__main__':
    main()