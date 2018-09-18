# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import arrow
import git_base
import log_utils
import re

logger = log_utils.get_logger()
release_prefix = 'release_'
dev_prefix = 'dev_'


# main test function
def main():
    # git_base.checkGitRepoStatus('/Users/pofy/Documents/projects_py/GitTools')
    create_next_week_branch('release_20180927',
                            '/Users/pofy/Documents/projects_py/GitTools')


# 创建下周分支
def create_next_week_branch(current_week_branch, work_path):
    print('准备开始创建下周分支', '当前分支:', current_week_branch)
    try:
        current_branch_trans_time = arrow.now().format('YYYYMMDD')
        logger.info('当前日期:' + current_branch_trans_time)

        next_version_date = arrow.utcnow().shift(weekday=3).format('YYYYMMDD')
        logger.info('下期版本日期:' + next_version_date)

        # next dev branch name
        next_dev_branch = dev_prefix + next_version_date

        # next release branch name
        next_release_branch = release_prefix + next_version_date
        logger.info('下期版本分支:' + next_dev_branch + '/' + next_release_branch)

        # create branch
        logger.info('开始创建下期分支.')
        git_base.create_local_branch(next_dev_branch, work_path)
        git_base.create_local_branch(next_release_branch, work_path)
        # 推送分支到远端(需要检查远端是否限制Push权限))
        # git_base.push_branch_to_remote(work_path, 'origin',
        #                                next_version_branch)
    except Exception as e:
        logger.info('创建下周分支过程出错' + e)


# 根据stdout获取当前分支
def get_current_branch(stdout):
    if (stdout != ''):
        start_index = stdout.find('*')
        end_index = stdout.find('\n', start_index)
        logger.info('当前分支：' + stdout[start_index + 2:end_index])
    else:
        logger.info('stdout为空！')
    return stdout[start_index + 2:end_index]


# 检查分支是否存在
def check_branch_exist(branch_name, stdout):
    try:
        str_array = stdout.split('\n')
        result_str = ''
        for str in str_array:
            if (str != ''):
                result_str = result_str + re.sub('\s', '', str) + ','
        print('分支已存在，请检出')
        index = result_str.index(branch_name)
        return True
    except Exception as e:
        print('分支不存在，可以进行创建', e)
        return False


# 获取最新分支  dev & release branch
def get_lastest_branch(stdout):
    try:
        str_array = stdout.split('\n')
        result_array = []
        # 远端分支list
        remote_array = []
        for str in str_array:
            if (str != ''):
                result_array.append(str)
            # 字符串去空处理
            str_nospace = re.sub('\s', '', str)
            if (str_nospace.startswith('remotes/origin/dev')
                    or str_nospace.startswith('remotes/origin/release')):
                remote_array.append(str_nospace)
        result_array.sort()
        print('============result array====================')
        print('result array:', result_array)
        print('============remote branch===================')
        print('remote branch array:', remote_array)
        print('============branch count====================')
        print('branch counts:', len(result_array))
        return 0
    except Exception as e:
        print('get lastest branch error')
        return -1


if __name__ == '__main__':
    main()
