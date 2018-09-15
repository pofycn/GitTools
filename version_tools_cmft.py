# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import arrow
import git_base


# main test function
def main():
    # git_base.checkGitRepoStatus('/Users/pofy/Documents/projects_py/GitTools')
    create_next_week_branch('release_20180927',
                            '/Users/pofy/Documents/projects_py/GitTools')


# 创建下周分支
def create_next_week_branch(current_week_branch, work_path):
    print('准备开始创建下周分支', '当前分支:', current_week_branch)
    try:
        current_branch_prefix = str.rsplit(current_week_branch, '_', -1)[0]
        current_branch_date = str.rsplit(current_week_branch, '_', -1)[1]
        current_branch_trans_time = arrow.get(current_branch_date, 'YYYYMMDD')
        print('当前分支日期:', current_branch_trans_time)
        next_version_date = current_branch_trans_time.shift(days=+7)
        print('下期版本日期:', next_version_date)
        next_version_branch = current_branch_prefix + '_' + str(
            next_version_date.format('YYYYMMDD'))
        print('下期版本分支:', next_version_branch)
        print('创建下期分支')
        git_base.create_local_branch(next_version_branch, work_path)
        # 推送分支到远端(需要检查远端是否限制Push权限))
        # git_base.push_branch_to_remote(work_path, 'origin',
        #                                next_version_branch)
    except Exception as e:
        print('创建下周分支过程出错', e)


if __name__ == '__main__':
    main()
