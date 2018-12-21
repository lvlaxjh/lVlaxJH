#!/usr/bin/env python

import paramiko

if "__main__" == __name__:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        ssh.connect('47.93.36.54', 22, 'root', 'jhczxcvbnm0325!!!')
        ml=input('执行命令:')
        stdin, stdout, stderr = ssh.exec_command(ml)
        print(stdout.readlines())
        ssh.close()