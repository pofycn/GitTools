# -*- coding: utf-8 -*-
import subprocess
import os


# 查看工作区状态
def checkGitRepoStatus():
    print('获取当前目录:', os.path.abspath(os.path.dirname(__file__)))
    execCmd = ['git', 'status']
    print('开始检查git工作区状态...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '获取git工作区状态')
    return result


# 将修改的文件添加到工作区
def addAllChangesToStatge():
    execCmd = ['git', 'add', '.']
    print('开始将更新后的文件添加到工作区...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '将更新后的文件添加到工作区')
    return result


# 提交更新
def commitChanges():
    execCmd = [
        'git', 'commit', '-m', '"auto commit by gittools powered by POFY"'
    ]
    print('准备提交更新至本地库...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '提交更新至本地库')
    return result


# 查看本地分支
def checkLocalBranch():
    execCmd = ['bash', 'sh/checkLocalBranch.sh']
    print('查看本地分支...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '查看本地分支')
    return result


# 创建本地分支
def createLocalBranch(branchName):
    execCmd = 'git checkout -b ' + branchName
    print('准备创建本地分支...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '创建本地分支')
    return result


# 删除本地分支
def deleteLocalBranch(branchName):
    execCmd = 'git checkout master && git branch -D ' + branchName
    print('准备删除本地分支...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '删除本地分支')
    return result


# 为master创建TAG
def createTag(tagName):
    execCmd = 'git checkout master && git tag ' + tagName
    print('准备创建Tag...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '创建Tag')
    return result


# 删除tag
def deleteTag(tagName):
    execCmd = 'git tag -d ' + tagName
    print('准备删除Tag...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '删除Tag')
    return result


# 推送tag至远端
def pushTag(tagName):
    execCmd = 'git push origin ' + tagName
    print('准备推送Tag至远端...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '推送Tag至远端')
    return result


# 更新远端索引
def fetchIndex():
    execCmd = 'git fetch'
    print('准备更新远端索引...')
    returnCode = executeCommand(execCmd)
    result = checkExecutionResult(returnCode, '更新远端索引')
    return result


# 执行命令
def executeCommand(execCmd):
    try:
        print('-----------------command result start. ----------------')
        # childProcess = subprocess.Popen(execCmd, shell=True)
        childProcess = subprocess.Popen(
            execCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print('output string:', childProcess.stdout.read())
        stdout, stderr = childProcess.communicate()
        print('stdout begin-----')
        print(stdout)
        print('stdout end  -----\n')
        print('stderr begin-----')
        print(stderr)
        print('stderr end  -----\n')
        # childProcess.wait()
        print('-----------------command result end.   ----------------')
        print('命令执行完成,exit with code:', childProcess.returncode)
        return childProcess.returncode
    finally:
        childProcess.kill()


# 检查命令执行结果
def checkExecutionResult(returnCode, message):
    if returnCode != 0:
        print(message, '--', '失败\n')
        return False
    else:
        print(message, '--', '成功\n')
        return True


def main():
    if (checkGitRepoStatus()):
        if (addAllChangesToStatge()):
            commitChanges()
    # checkLocalBranch()
    # createLocalBranch('dev')
    # deleteLocalBranch('dev')
    # executeCommand('')


if __name__ == '__main__':
    main()
