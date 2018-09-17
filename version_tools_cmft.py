# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import arrow
import git_base
import log_utils

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
        logger.info('开始创建下期分支.')
        git_base.create_local_branch(next_dev_branch, work_path)
        git_base.create_local_branch(next_release_branch, work_path)
        # 推送分支到远端(需要检查远端是否限制Push权限))
        # git_base.push_branch_to_remote(work_path, 'origin',
        #                                next_version_branch)
    except Exception as e:
        logger.info('创建下周分支过程出错' + e)


if __name__ == '__main__':
    main()
