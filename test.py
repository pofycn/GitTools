# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import git_base


def main():
    # cmd = ['cd', '..']
    _, stdout, stderr = git_base.checkLocalBranch()
    print(stdout)


if __name__ == '__main__':
    main()
