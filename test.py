# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import re
import git_base
import log_utils


def main():
    log_utils.clear_log_content()
    result, stdout, stderr = git_base.check_local_branch(
        '/Users/pofy/Documents/projects_py/GitTools')

    # logger.info('\n-----------stdout-----------')
    # logger.info('\n' + stdout)

    # logger.info('\n-----------stderr-----------')
    # logger.info('\n' + stderr)

    # logger.info('\n-----------branch-----------')

    # print(log_utils.read_logs())
    # print('\nreturn code:', returnCode)


def get_current_branch(stdout):
    print('当前分支:')
    start_index = stdout.find('*')
    end_index = stdout.find('\n')
    print(stdout[start_index + 2:end_index])


if __name__ == '__main__':
    main()