# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import re
import git_base


def main():
    result,stdout,stderr=git_base.check_local_branch('/Users/pofy/Documents/projects_py/GitTools')
    print('-----------stdout-----------')
    print(stdout)

    print('\n-----------stderr-----------')
    print(stderr)

    print('\n-----------branch-----------')
    get_current_branch(stdout)

    # print('\nreturn code:', returnCode)

def get_current_branch(stdout):
    print('当前分支:')
    start_index=stdout.find('*')
    end_index=stdout.find('\n')
    print(stdout[start_index+2:end_index])
if __name__ == '__main__':
    main()
