# -*- coding: utf-8 -*-
import subprocess
import os

# 查看工作区状态
def checkGitRepoStatus():
    print('获取当前目录:',os.path.abspath(os.path.dirname(__file__)))
    execCmd = 'git status'
    print('开始检查git status...')
    returnCode = executeCommand(execCmd)
    print('命令执行完成...')
    if returnCode != 0:
        print('获取git工作区状态失败...')
        return False
    else:
        print('获取git工作区状态成功...')
        return True

# 将修改的文件添加到工作区
def addAllChangesToStatge():
    execCmd='git add .'
    print('开始将更新后的文件添加到工作区...')
    print(execCmd)
    returnCode = executeCommand(execCmd)
    print('命令执行完成...')
    if returnCode != 0:
        print('添加至git仓库失败...')
        return False
    else:
        print('添加至git仓库成功...')
        return True

def commitChanges():
    execCmd='git commit -m "auto commit by gittools power by POFY"'
    print('准备提交更新至本地库...')
    returnCode=executeCommand(execCmd)
    print('命令执行完成...')
    if returnCode != 0:
        print('提交更新至本地库失败...')
        return False
    else:
        print('提交更新至本地库成功...')
        return True
    
def executeCommand(execCmd):
    print('-----------------command result start-----------------')
    print(execCmd)
    process = subprocess.Popen(execCmd, shell=True)
    process.wait()
    print('-----------------command result end-------------------')
    return process.returncode

def main():
    if(checkGitRepoStatus()):
        if(addAllChangesToStatge()):
            commitChanges()


if __name__ == '__main__':
    main()
