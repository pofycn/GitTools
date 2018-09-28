# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import arrow
import git_base
import log_utils
import gitlab_tools
import re

RELEASE_PREFIX = 'release_'
DEV_PREFIX = 'dev_'
REMOTE_DEVBRANCH_PREFIX = 'dev'
REMOTE_RELEASEBRANCH_PREFIX = 'release'
MASTER = 'master'
BRANCH_CHECK_STATUS = 0
BRANCH_CHECK_DEV_EXIST = 1
BRANCH_CHECK_RELEASE_EXIST = 2
BRANCH_CHECK_BOTH_EXIST = 3
FRIDAY = 'Fri'

logger = log_utils.get_logger()


# 创建下周分支
def create_next_week_branch(project_id):
    logger.info('准备创建下周分支')
    try:
        now = arrow.utcnow()
        current_branch_trans_time = now.format('YYYYMMDD')
        current_weekday = arrow.utcnow().format('ddd')
        logger.info('当前日期:' + current_branch_trans_time + ' ' +
                    current_weekday)

        if (current_weekday == FRIDAY):
            now = now.shift(days=-1)

        next_version_date = now.shift(weekday=3).shift(
            weeks=+1).format('YYYYMMDD')
        logger.info('下期版本日期:' + next_version_date)

        # _, stdout, _ = git_base.check_local_branch(work_path)

        branch_name_list = gitlab_tools.get_branches_names_by_project_id(
            project_id)
        # get lastest branch
        dev_remote, release_remote = get_lastest_branch(branch_name_list)

        logger.info('最新dev分支:' + dev_remote)
        logger.info('最新release分支:' + release_remote)

        next_branch_check_flag = BRANCH_CHECK_STATUS

        # next dev branch name
        next_dev_branch = DEV_PREFIX + next_version_date
        if (next_dev_branch == dev_remote):
            next_branch_check_flag += 1

        # next release branch name
        next_release_branch = RELEASE_PREFIX + next_version_date
        if (next_release_branch == release_remote):
            next_branch_check_flag += 2

        # check dev or release branches already exist
        if (next_branch_check_flag == BRANCH_CHECK_DEV_EXIST):
            logger.info('下周版本dev分支已经存在，无需创建，请检出对应分支')
            return
        elif (next_branch_check_flag == BRANCH_CHECK_RELEASE_EXIST):
            logger.info('下周release分支已经存在，无需创建，请检出对应分支')
            return
        elif (next_branch_check_flag == BRANCH_CHECK_BOTH_EXIST):
            logger.info('下周 dev & release 分支已经存在，无需创建，请检出对应分支')
            return

        logger.info('下期版本分支:' + next_dev_branch + '/' + next_release_branch)

        # create dev branch
        logger.info('\n开始创建下周dev分支.')
        gitlab_tools.create_branch(project_id, next_dev_branch, dev_remote)

        # create release branch
        logger.info('\n开始创建下周release分支.')
        gitlab_tools.create_branch(project_id, next_release_branch,
                                   release_remote)
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
        logger.info('分支已存在，请检出')
        index = result_str.index(branch_name)
        return True
    except Exception as e:
        logger.info('分支不存在，可以进行创建', e)
        return False


# 获取远端新分支
def get_lastest_branch(branch_name_list):
    try:
        # 远端分支list
        remote_dev_array = []
        remote_release_array = []
        for str in branch_name_list:
            # 字符串去空处理
            str_nospace = re.sub('\s', '', str)

            if (str_nospace.startswith(REMOTE_DEVBRANCH_PREFIX)):
                remote_dev_array.append(str_nospace)

            if (str_nospace.startswith(REMOTE_RELEASEBRANCH_PREFIX)):
                remote_release_array.append(str_nospace)

        # 以分支名对分支List进行排序
        remote_dev_array.sort()
        remote_release_array.sort()

        # 计算dev,release分支的数量
        # 如果dev、release分支没有最新分支，则以默认master分支为两类分支的最新分支
        counts_remote_dev = len(remote_dev_array)
        if (counts_remote_dev == 0):
            counts_remote_dev += 1
            remote_dev_array.append(MASTER)

        counts_remote_release = len(remote_release_array)
        if (counts_remote_release == 0):
            counts_remote_release += 1
            remote_release_array.append(MASTER)

        return remote_dev_array[counts_remote_dev - 1], remote_release_array[
            counts_remote_release - 1]
    except Exception as e:
        logger.info('查看最新版本分支错误')
        return -1


# main test function
def main():
    print('====================test====================')
    # git_base.checkGitRepoStatus('/Users/pofy/Documents/projects_py/GitTools')
    # create_next_week_branch(1174)

    # delete_branch(1174, 'dev')
    # delete_branch(1174, 'release')


if __name__ == '__main__':
    main()
