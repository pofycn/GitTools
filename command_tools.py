# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess
import log_utils


# 执行命令
def execute_command(exec_cmd, work_path):
    logger = log_utils.get_logger()
    try:
        childProcess = subprocess.Popen(
            exec_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_path)
        stdout, stderr = childProcess.communicate()
        childProcess.wait()
        returnCode = childProcess.returncode
        # LOGGER.info('命令执行完成,exit with code:' + returnCode)
        return returnCode, str(stdout, 'UTF-8'), str(stderr, 'UTF-8')
    except Exception as e:
        print('执行命令过程出现异常\n', e)
    finally:
        if childProcess.poll() != 0:
            childProcess.kill()


# 检查命令执行结果
def check_execution_result(return_code, message, stdout, stderr):
    logger = log_utils.get_logger()
    if return_code != 0:
        logger.info(message + '--' + '失败!')
        logger.info('结果:')
        logger.info(stderr)
        return False
    else:
        logger.info(message + '--' + '成功!')
        logger.info('结果:')
        logger.info(stdout)
        return True


def notify():
    print('Don\'t run command tools directly~')


if __name__ == '__main__':
    notify()
