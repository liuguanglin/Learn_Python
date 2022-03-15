#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pycurl

url = 'https://www.w3.org'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.SSL_VERIFYPEER, 0)  # 不进行SSL校验
c.setopt(pycurl.USERAGENT, user_agent)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
curl_file = open('curl_ctx.txt', 'wb')
c.setopt(pycurl.WRITEHEADER, curl_file)
c.setopt(pycurl.WRITEDATA, curl_file)
c.perform()
curl_file.close()

print('HTTP状态码: ', c.getinfo(c.HTTP_CODE))
print(f'DNS解析时间: {c.getinfo(c.NAMELOOKUP_TIME)}s')
print(f'TCP连接耗时: {c.getinfo(c.CONNECT_TIME)}s')
print(f'HTTP连接之前所耗时: {c.getinfo(c.APPCONNECT_TIME)}s')
print(f'开始传输之前所耗时: {c.getinfo(c.PRETRANSFER_TIME)}s')
print(f'开始传输所耗时: {c.getinfo(c.STARTTRANSFER_TIME)}s')  # 此时为接收到第一个字节的数据
print(f'总时间: {c.getinfo(c.TOTAL_TIME)}s')
print(f'下载大小: {c.getinfo(c.SIZE_DOWNLOAD)} bytes')
print(f'头部大小: {c.getinfo(c.HEADER_SIZE)} bytes')
print(f'下载速度: {c.getinfo(c.SPEED_DOWNLOAD)/1024} kB/s')
