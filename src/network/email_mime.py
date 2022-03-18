#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from_addr = 'user@example'
passwd = 'password'
to_addrs = ['user1@example', 'user2@example']
cc = ['user3@example', 'user4@example']
subject = '邮件附件测试'
msg_text = MIMEText("""<div style="background-color:#bfa;"><h2>这是测试邮件</h2>
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/17/Draw_email.png" alt="email" /><br />
            这是一个<a href="https://www.w3.org/">链接</a><br />
            附加一张图片<img src="cid:myimg"></div>""", 'html', 'utf-8')


def add_img(src, cid):
    with open(src, 'rb') as f:
        att_img = MIMEImage(f.read())
    att_img.add_header('Content-ID', cid)
    msg.attach(att_img)


def att_file(src, att_name):
    with open(src, 'rb') as f:
        att = MIMEApplication(f.read())
    att.add_header('Content-Disposition', 'attachment', filename=att_name)
    msg.attach(att)


msg = MIMEMultipart()
msg.attach(msg_text)
add_img('myimg.png', 'myimg')
att_file('file.zip', '附件.zip')
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = ', '.join(to_addrs)
msg['Cc'] = ', '.join(cc)
smtp_server = 'smtp.server'
smtp_port = 465

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.set_debuglevel(2)
    server.login(from_addr, passwd)
    server.sendmail(from_addr, to_addrs + cc, msg.as_string())
