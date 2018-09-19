# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import arrow
import git_base
import log_utils
import re

RELEASE_PREFIX = 'release_'
DEV_PREFIX = 'dev_'
LOCAL_DEVBRANCH_PREFIX = 'dev'
LOCAL_RELEASEBRANCH_PREFIX = 'release'
REMOTE_DEVBRANCH_PREFIX = 'remotes/origin/dev'
REMOTE_RELEASEBRANCH_PREFIX = 'remotes/origin/release'
REMOTE_ORIGIN_PREFIX = 'remotes/origin/'
REMOTE_ORIGIN = 'origin/'
EMPTY = 'EMPTY'
logger = log_utils.get_logger()


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

        _, stdout, _ = git_base.check_local_branch(work_path)
        # get lastest branch
        dev_local, release_local, dev_remote, release_remote = get_lastest_branch(
            stdout)

        logger.info('最新本地及远端分支:' + dev_local + ',' + release_local + ',' +
                    dev_remote + ',' + release_remote)
        # next dev branch name
        next_dev_branch = DEV_PREFIX + next_version_date
        if (next_dev_branch == dev_local or next_dev_branch == dev_remote):
            logger.info('下周dev分支已经存在，无需创建，请按需检出对应分支')
            return

        # next release branch name
        next_release_branch = RELEASE_PREFIX + next_version_date
        if (next_release_branch == release_local
                or next_release_branch == release_remote):
            logger.info('下周dev分支已经存在，无需创建，请按需检出对应分支')
            return
        logger.info('下期版本分支:' + next_dev_branch + '/' + next_release_branch)

        # create dev branch
        logger.info('开始创建下周dev分支.')
        if (dev_local != EMPTY and dev_remote != EMPTY):
            if (dev_local < dev_remote):
                logger.info('远端分支时间线晚于本地分支---将以远端最新分支创建下周dev分支')
                git_base.checkout_branch_from_remote(
                    next_dev_branch, REMOTE_ORIGIN + dev_remote, work_path)
            else:
                logger.info('本地分支时间线晚于远端分支---将以本地最新分支创建下周dev分支')
                git_base.checkout_branch(dev_local, work_path)
                git_base.create_local_branch(next_dev_branch, work_path)
        else:
            # 以默认分支创建下周分支
            logger.info('默认以当前分支创建下周分支')
            git_base.create_local_branch(next_dev_branch, work_path)

        # create release branch
        logger.info('开始创建下周release分支.')
        if (release_local != EMPTY and release_remote != EMPTY):
            if (release_local < release_remote):
                logger.info('远端分支时间线晚于本地分支---将以远端最新分支创建下周release分支')
                git_base.checkout_branch_from_remote(
                    next_release_branch, REMOTE_ORIGIN + dev_remote, work_path)
            else:
                logger.info('本地分支时间线晚于远端分支---将以本地最新分支创建下周release分支')
                git_base.checkout_branch(dev_local, work_path)
                git_base.create_local_branch(next_release_branch, work_path)
        else:
            # 以默认分支创建下周分支
            _, all_branch_info, _ = git_base.check_local_branch(work_path)
            current_branch_name = get_current_branch(all_branch_info)
            logger.info('默认以当前分支创建下周分支:' + current_branch_name)
            git_base.create_local_branch(next_release_branch, work_path)

        # checkout local branch dev to the lastest
        # git_base.create_local_branch(next_dev_branch, work_path)
        # checkout local branch dev to the lastest
        # git_base.create_local_branch(next_release_branch, work_path)
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


# 获取最新分支  local & remote --- dev & release branch
def get_lastest_branch(stdout):
    try:
        str_array = stdout.split('\n')
        result_array = []
        local_dev_array = []
        local_release_array = []
        # 远端分支list
        remote_dev_array = []
        remote_release_array = []
        for str in str_array:
            # 字符串去空处理
            str_nospace = re.sub('\s', '', str)

            if (str_nospace.find('*') != -1):
                str_nospace = str_nospace.replace('*', '')

            if (str_nospace.startswith(LOCAL_DEVBRANCH_PREFIX)):
                local_dev_array.append(str_nospace)

            if (str_nospace.startswith(LOCAL_RELEASEBRANCH_PREFIX)):
                local_release_array.append(str_nospace)

            if (str_nospace.startswith(REMOTE_DEVBRANCH_PREFIX)):
                remote_dev_array.append(
                    str_nospace.split(REMOTE_ORIGIN_PREFIX)[1])

            if (str_nospace.startswith(REMOTE_RELEASEBRANCH_PREFIX)):
                remote_release_array.append(
                    str_nospace.split(REMOTE_ORIGIN_PREFIX)[1])

        # print('============local dev branch================')
        local_dev_array.sort()
        # print('local dev branch array:', local_dev_array)

        # print('============local dev branch================')
        local_release_array.sort()
        # print('local release branch array:', local_release_array)

        # print('============remote dev branch===============')
        remote_dev_array.sort()
        # print('remote dev branch array:', remote_dev_array)

        # print('============remote release branch===========')
        remote_release_array.sort()
        # print('remote dev branch array:', remote_release_array)

        print('============branch count====================')
        counts_local_dev = len(local_dev_array)
        if (counts_local_dev == 0):
            counts_local_dev = counts_local_dev + 1
            local_dev_array.append(EMPTY)

        counts_local_release = len(local_release_array)
        if (counts_local_release == 0):
            counts_local_release += 1
            local_release_array.append(EMPTY)

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
        return local_dev_array[counts_local_dev - 1], local_release_array[
            counts_local_release -
            1], remote_dev_array[counts_remote_dev - 1], remote_release_array[
                counts_remote_release - 1]
    except Exception as e:
        logger.info('查看最新版本分支错误')
        return -1


if __name__ == '__main__':
    main()
