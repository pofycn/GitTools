# -*- coding: utf-8 -*-

'Git tools base lib'

__author__ = 'Jerry Chan'

import subprocess
import os


# 查看工作区状态
def checkGitRepoStatus():
    print('获取当前目录:', os.path.abspath(os.path.dirname(__file__)))
    execCmd = ['git', 'status']
    print('开始检查git工作区状态...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '获取git工作区状态', stdout, stderr)
    return result


# 将修改的文件添加到工作区
def addAllChangesToStatge():
    execCmd = ['git', 'add', '.']
    print('开始将更新后的文件添加到工作区...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '将更新后的文件添加到工作区', stdout, stderr)
    return result


# 提交更新
def commitChanges():
    execCmd = [
        'git', 'commit', '-m', '"auto commit by gittools powered by POFY"'
    ]
    print('准备提交更新至本地库...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '提交更新至本地库', stdout, stderr)
    return result


# 查看本地分支
def checkLocalBranch():
    execCmd = ['bash', 'sh/checkLocalBranch.sh']
    print('准备查看本地分支...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '查看本地分支', stdout, stderr)
    return result


# 切换分支
def checkoutBranch(branchName):
    execCmd = ['git', 'checkout', branchName]
    print('准备切换分支...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '切换分支', stdout, stderr)
    return result


# 创建本地分支
def createLocalBranch(branchName):
    execCmd = ['git', 'checkout', '-b', branchName]
    print('准备创建本地分支...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '创建本地分支', stdout, stderr)
    return result


# 删除本地分支
def deleteLocalBranch(branchName):
    checkoutBranch('master')
    execCmd = ['git', 'branch', '-D', branchName]
    print('准备删除本地分支...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '删除本地分支', stdout, stderr)
    return result


# 为master创建TAG
def createTag(tagName):
    checkoutBranch('master')
    execCmd = ['git', 'tag', tagName]
    print('准备创建Tag...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '创建Tag', stdout, stderr)
    return result


# 删除tag
def deleteTag(tagName):
    execCmd = ['git', 'tag', '-d', tagName]
    print('准备删除Tag...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '删除Tag', stdout, stderr)
    return result


# 推送tag至远端
def pushTag(tagName):
    execCmd = ['git', 'push', 'origin', tagName]
    print('准备推送Tag至远端...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '推送Tag至远端', stdout, stderr)
    return result


# 更新远端索引
def fetchIndex():
    execCmd = ['git', 'fetch']
    print('准备更新远端索引...')
    returnCode, stdout, stderr = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '更新远端索引', stdout, stderr)
    return result


# 执行命令
def executeCommand(execCmd):
    try:
        childProcess = subprocess.Popen(
            execCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = childProcess.communicate()
        childProcess.wait()
        returnCode = childProcess.returncode
        print('命令执行完成,exit with code:', returnCode)
        return returnCode, str(stdout, 'UTF-8'), str(stderr, 'UTF-8')
    finally:
        if childProcess.poll() != 0:
            childProcess.kill()


# 检查命令执行结果
def checkExecutionResult(returnCode, message, stdout, stderr):
    if returnCode != 0:
        print(message, '--', '失败!\n')
        print('结果:')
        print(stderr)
        return False
    else:
        print(message, '--', '成功!\n')
        print('结果:')
        print(stdout)
        return True


# def main():
# if (checkGitRepoStatus()):
#     if (addAllChangesToStatge()):
#         commitChanges()
# checkLocalBranch()
# createLocalBranch('dev')
# deleteLocalBranch('dev')
# executeCommand('')


def notify():
    print('don\'t run gitbase directly~')


if __name__ == '__main__':
    notify()
