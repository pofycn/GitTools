# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import re
import git_base
import log_utils
import arrow
import version_tools_cmft as cmft_tools


def main():
    # log_utils.clear_log_content()
    # result, stdout, stderr = git_base.check_local_branch(
    #     '/Users/pofy/Documents/projects_py/GitTools')

    # arw = arrow.utcnow()
    # next_arw=arw.shift(weekday=3).format('YYYYMMDD')
    # print(next_arw)

    # path1: /Users/pofy/Documents/projects_py/GitTools
    # path2: /Users/pofy/Documents/projects/shop-app
    result, stdout, stderr = git_base.check_local_branch(
        '/Users/pofy/Documents/projects_py/GitTools')
    print('=========================测试=========================')
    print(cmft_tools.check_branch_exist('master', stdout))
    print(cmft_tools.get_lastest_branch(stdout))


if __name__ == '__main__':
    main()