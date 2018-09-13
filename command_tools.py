# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess


# 执行命令
def execute_command(exec_cmd, work_path):
    try:
        childProcess = subprocess.Popen(
            exec_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_path)
        stdout, stderr = childProcess.communicate()
        childProcess.wait()
        returnCode = childProcess.returncode
        print('命令执行完成,exit with code:', returnCode)
        return returnCode, str(stdout, 'UTF-8'), str(stderr, 'UTF-8')
    finally:
        if childProcess.poll() != 0:
            childProcess.kill()


# 检查命令执行结果
def check_execution_result(return_code, message, stdout, stderr):
    if return_code != 0:
        print(message, '--', '失败!\n')
        print('结果:')
        print(stderr)
        return False
    else:
        print(message, '--', '成功!\n')
        print('结果:')
        print(stdout)
        return True


def notify():
    print('Don\'t run command tools directly~')


if __name__ == '__main__':
    notify()
