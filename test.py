# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import subprocess


def main():
    cmd = ['ls', '-ah']
    path = '/Users/pofy/Documents/tools'
    # returnCode, stdout, stderr = command_tools.executeCommand(cmd)
    childProcess = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)

    stdout, stderr = childProcess.communicate()
    print('-----------stdout-----------')
    print(str(stdout, 'UTF-8'))

    print('\n-----------stderr-----------')
    print(str(stderr, 'UTF-8'))

    # print('\nreturn code:', returnCode)


if __name__ == '__main__':
    main()
