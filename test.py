# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import re
import git_base
import log_utils
import arrow


def main():
    # log_utils.clear_log_content()
    # result, stdout, stderr = git_base.check_local_branch(
    #     '/Users/pofy/Documents/projects_py/GitTools')
    arw = arrow.utcnow()
    next_arw=arw.shift(weekday=3).format('YYYYMMDD')
    print(next_arw)


def get_current_branch(stdout):
    print('当前分支:')
    start_index = stdout.find('*')
    end_index = stdout.find('\n')
    print(stdout[start_index + 2:end_index])


if __name__ == '__main__':
    main()