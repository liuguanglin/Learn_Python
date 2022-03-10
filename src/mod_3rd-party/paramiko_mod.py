#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko
import os


def ssh_conn(hostname, username, password, pkey):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
    # ssh.connect(hostname=hostname, username=username, password=password)
    ssh.connect(hostname=hostname, username=username, pkey=pkey)
    stdin, stdout, stderr = ssh.exec_command('df -Th')
    print('Command results:\n', stdout.read().decode())
    ssh.close()


def sftp_trans(hostname, username, password, pkey):
    trans = paramiko.Transport((hostname, 22))
    # trans.connect(username=username, password=password)
    trans.connect(username=username, pkey=pkey)
    sftp = paramiko.SFTPClient.from_transport(trans)

    sftp.chdir('/tmp')
    print('Current dir:', sftp.getcwd())
    sftp.mkdir('ftp_dir')
    sftp.rmdir('ftp_dir')
    sftp.put('/etc/hostname', 'local_hostname')
    sftp.get('/etc/hosts', 'remote_hosts')
    print('list dir: ', sftp.listdir())
    trans.close()


if __name__ == '__main__':
    host = 'node1'
    user = 'root'
    passwd = 'pass123'
    pri_key = paramiko.RSAKey.from_private_key_file(os.path.expanduser('~/.ssh/id_rsa'))
    paramiko.util.log_to_file('ssh.log')

    ssh_conn(host, user, passwd, pri_key)
    sftp_trans(host, user, passwd, pri_key)
