#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib

from_addr = 'user@example'
passwd = 'password'
to_addrs = ['user1@example', 'user2@example']
cc = ['user3@example', 'user4@example']
subject = '纯文本邮件测试'
msg_cont = """越过长城，走向世界。\nHello,world."""
msg = f'From: {from_addr}\nTo: {", ".join(to_addrs)}\nCc: {", ".join(cc)}\nSubject: {subject}\n{msg_cont}'

smtp_server = 'smtp.server'
smtp_port = 465

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.set_debuglevel(2)
    server.login(from_addr, passwd)
    server.sendmail(from_addr, to_addrs + cc, msg.encode())
