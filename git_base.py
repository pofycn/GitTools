# -*- coding: utf-8 -*-

'Git tools base lib'

__author__ = 'Jerry Chan'

import os
import command_tools
import log_utils



# 查看工作区状态
def check_git_repo_status(work_path):
    print('获取当前目录:' , os.path.abspath(os.path.dirname(__file__)))
    exec_cmd = ['git', 'status']
    print('开始检查git工作区状态...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '获取git工作区状态',
                                                  stdout, stderr)
    return result, stdout, stderr


# 将修改的文件添加到工作区
def add_all_changes_to_statge(work_path):
    exec_cmd = ['git', 'add', '.']
    print('开始将更新后的文件添加到工作区...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '将更新后的文件添加到工作区',
                                                  stdout, stderr)
    return result, stdout, stderr


# 提交更新
def commit_changes(work_path):
    exec_cmd = [
        'git', 'commit', '-m', '"auto commit by gittools powered by POFY"'
    ]
    print('准备提交更新至本地库...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '提交更新至本地库',
                                                  stdout, stderr)
    return result, stdout, stderr


# Push本地分支至远端
def push_branch_to_remote(work_path, remote_name, remote_branch):
    exec_cmd = ['git', 'push', remote_name, remote_branch]
    print('准备提交更新至远端...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '提交更新至远端',
                                                  stdout, stderr)
    return result, stdout, stderr


# 查看本地分支
def check_local_branch(work_path):
    logger = log_utils.get_logger()
    exec_cmd = ['git', 'branch', '-a']
    logger.info('准备查看本地分支...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '查看本地分支', stdout,
                                                  stderr)
    return result, stdout, stderr


# 切换分支
def checkout_branch(branch_name, work_path):
    exec_cmd = ['git', 'checkout', branch_name]
    print('准备切换分支...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '切换分支', stdout,
                                                  stderr)
    return result, stdout, stderr


# 创建本地分支
def create_local_branch(branch_name, work_path):
    exec_cmd = ['git', 'checkout', '-b', branch_name]
    print('准备创建本地分支...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '创建本地分支', stdout,
                                                  stderr)
    return result, stdout, stderr


# 删除本地分支
def delete_local_branch(branch_name, work_path):
    checkout_branch('master', work_path)
    exec_cmd = ['git', 'branch', '-D', branch_name]
    print('准备删除本地分支...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '删除本地分支', stdout,
                                                  stderr)
    return result, stdout, stderr


# 为master创建TAG
def create_tag(tag_name, work_path):
    checkout_branch('master', work_path)
    exec_cmd = ['git', 'tag', tag_name]
    print('准备创建Tag...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '创建Tag', stdout,
                                                  stderr)
    return result, stdout, stderr


# 删除tag
def delete_tag(tag_name, work_path):
    exec_cmd = ['git', 'tag', '-d', tag_name]
    print('准备删除Tag...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '删除Tag', stdout,
                                                  stderr)
    return result, stdout, stderr


# 推送tag至远端
def push_tag(tag_name, work_path):
    exec_cmd = ['git', 'push', 'origin', tag_name]
    print('准备推送Tag至远端...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '推送Tag至远端',
                                                  stdout, stderr)
    return result, stdout, stderr


# 更新远端索引
def fetch_index(work_path):
    exec_cmd = ['git', 'fetch']
    print('准备更新远端索引...')
    returnCode, stdout, stderr = command_tools.execute_command(
        exec_cmd, work_path)
    result = command_tools.check_execution_result(returnCode, '更新远端索引', stdout,
                                                  stderr)
    return result, stdout, stderr


# def main():
# if (checkGitRepoStatus()):
#     if (addAllChangesToStatge()):
#         commitChanges()
# checkLocalBranch()
# createLocalBranch('dev')
# deleteLocalBranch('dev')
# executeCommand('')


def notify():
    print('Don\'t run gitbase directly~')


if __name__ == '__main__':
    notify()
