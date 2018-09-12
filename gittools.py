# -*- coding: utf-8 -*-
import subprocess
import os

# 查看工作区状态
def checkGitRepoStatus():
    print('获取当前目录:',os.path.abspath(os.path.dirname(__file__)))
    execCmd = 'git status'
    print('开始检查git status...')
    returnCode = executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'获取git工作区状态')
    return result

# 将修改的文件添加到工作区
def addAllChangesToStatge():
    execCmd='git add .'
    print('开始将更新后的文件添加到工作区...')
    print(execCmd)
    returnCode = executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'添加至git仓库')
    return result

# 提交更新
def commitChanges():
    execCmd='git commit -m "auto commit by gittools power by POFY"'
    print('准备提交更新至本地库...')
    returnCode=executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'提交更新至本地库')
    return result

# 查看本地分支
def checkLocalBranch():
    execCmd='git branch -a'
    print('查看本地所有分支...')
    returnCode=executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'查看本地')
    return result

# 创建本地分支
def createLocalBranch(branchName):
    execCmd='git checkout -b '+ branchName
    print('准备创建本地分支...')
    returnCode=executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'创建本地分支')
    return result

# 删除本地分支
def deleteLocalBranch(branchName):
    execCmd='git checkout master && git branch -D '+ branchName
    print('准备删除本地分支...')
    returnCode=executeCommand(execCmd)
    result=checkExecutionResult(returnCode,'删除本地分支')
    return result

# 执行命令    
def executeCommand(execCmd):
    print('-----------------command result start-----------------')
    print(execCmd)
    process = subprocess.Popen(execCmd, shell=True)
    process.wait()
    print('-----------------command result end-------------------')
    return process.returncode

# 检查命令执行结果
def checkExecutionResult(returnCode,message):
    if returnCode != 0:
        print(message,':','失败...')
        return False
    else:
        print(message,':','成功...')
        return True

def main():
    if(checkGitRepoStatus()):
        if(addAllChangesToStatge()):
            commitChanges()
    # checkLocalBranch()
    #reateLocalBranch('dev')
    # deleteLocalBranch('dev')


if __name__ == '__main__':
    main()
