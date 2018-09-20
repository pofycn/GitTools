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
REMOTE_ORIGIN_PREFIX = 'remotes/origin/'
REMOTE_ORIGIN = 'origin/'
EMPTY = 'EMPTY'
BRANCH_CHECK_DEFAULT = 0
BRANCH_CHECK_DEV_EXIST = 1
BRANCH_CHECK_RELEASE_EXIST = 2

logger = log_utils.get_logger()


# 创建下周分支
def create_next_week_branch(project_id):
    print('准备创建下周分支')
    try:
        current_branch_trans_time = arrow.now().format('YYYYMMDD')
        logger.info('当前日期:' + current_branch_trans_time)

        next_version_date = arrow.utcnow().shift(weekday=3).format('YYYYMMDD')
        logger.info('下期版本日期:' + next_version_date)

        # _, stdout, _ = git_base.check_local_branch(work_path)

        branch_name_list = gitlab_tools.get_branches_names_by_project_id(
            project_id)
        # get lastest branch
        dev_remote, release_remote = get_lastest_branch(branch_name_list)

        logger.info('最新远端分支:' + dev_remote + ',' + release_remote)

        next_branch_check_flag = BRANCH_CHECK_DEFAULT

        # next dev branch name
        next_dev_branch = DEV_PREFIX + next_version_date
        if (next_dev_branch == dev_remote):
            next_branch_check_flag = BRANCH_CHECK_DEV_EXIST

        # next release branch name
        next_release_branch = RELEASE_PREFIX + next_version_date
        if (next_release_branch == release_remote):
            next_branch_check_flag = BRANCH_CHECK_RELEASE_EXIST

        # check dev or release branches already exist
        if (next_branch_check_flag == BRANCH_CHECK_DEV_EXIST):
            logger.info('下周版本dev分支已经存在，无需创建，请检出对应分支')
            return
        elif (next_branch_check_flag == BRANCH_CHECK_RELEASE_EXIST):
            logger.info('下周release分支已经存在，无需创建，请检出对应分支')
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
        print('分支已存在，请检出')
        index = result_str.index(branch_name)
        return True
    except Exception as e:
        print('分支不存在，可以进行创建', e)
        return False


# 获取最新分支  local & remote --- dev & release branch
def get_lastest_branch(branch_name_list):
    try:
        result_array = []
        # 远端分支list
        remote_dev_array = []
        remote_release_array = []
        for str in branch_name_list:
            # 字符串去空处理
            str_nospace = re.sub('\s', '', str)

            if (str_nospace.startswith(REMOTE_DEVBRANCH_PREFIX)):
                remote_dev_array.append(
                    str_nospace.split(REMOTE_ORIGIN_PREFIX)[1])

            if (str_nospace.startswith(REMOTE_RELEASEBRANCH_PREFIX)):
                remote_release_array.append(
                    str_nospace.split(REMOTE_ORIGIN_PREFIX)[1])

        # print('============remote dev branch===============')
        remote_dev_array.sort()
        # print('remote dev branch array:', remote_dev_array)

        # print('============remote release branch===========')
        remote_release_array.sort()
        # print('remote dev branch array:', remote_release_array)

        print('============branch count====================')
        counts_remote_dev = len(remote_dev_array)
        if (counts_remote_dev == 0):
            counts_remote_dev += 1
            remote_dev_array.append(EMPTY)

        counts_remote_release = len(remote_release_array)
        if (counts_remote_release == 0):
            counts_remote_release += 1
            remote_release_array.append(EMPTY)

        # print('local dev branch counts:', counts_local_dev)
        # print('local release branch counts:', counts_local_release)

        # print('remote dev branch counts:', counts_remote_dev)
        # print('remote release branch counts:', counts_remote_release)
        return remote_dev_array[counts_remote_dev - 1], remote_release_array[
            counts_remote_release - 1]
    except Exception as e:
        logger.info('查看最新版本分支错误')
        return -1


# main test function
def main():
    # git_base.checkGitRepoStatus('/Users/pofy/Documents/projects_py/GitTools')
    create_next_week_branch(1174)


if __name__ == '__main__':
    main()
