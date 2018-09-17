# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import log_utils

logger = log_utils.get_logger()


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
        logger.info('命令执行完成,exit with code:' + str(returnCode))
        return returnCode, str(stdout, 'UTF-8'), str(stderr, 'UTF-8')
    except Exception as e:
        logger.info('执行命令过程出现异常:\n'+ e)
    finally:
        if childProcess.poll() != 0:
            childProcess.kill()


# 检查命令执行结果
def check_execution_result(return_code, message, stdout, stderr):
    if return_code != 0:
        logger.info(message + '：' + '失败!')
        logger.info('结果:')
        logger.info('\n' + stderr)
        return False
    else:
        logger.info(message + '：' + '成功!')
        logger.info('结果:')
        logger.info('\n' + stdout)
        return True


def notify():
    print('Don\'t run command tools directly~')


if __name__ == '__main__':
    notify()
