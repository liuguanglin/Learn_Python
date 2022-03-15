#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPy import IP, IPSet

print('IP类型')
print(IP('192.168.1.0/24').version())
print(IP('::1').version())

print('\n显示格式')
print(IP('192.168.1.0/24').strNormal())
print(IP('192.168.1.0/24').strNormal(0))
print(IP('192.168.1.0/24').strNormal(1))
print(IP('192.168.1.0/24').strNormal(2))
print(IP('192.168.1.0/24').strNormal(3))

print('\n子网容量: ', IP('192.168.1.0/28').len())
print('子网掩码: ', IP('172.17.0.0/18').netmask())
print('广播地址: ', IP('172.17.0.0/17').broadcast())
print('转换为对应的网络: ', IP('172.17.33.44').make_net('255.255.128.0'))

print('\n进制转换')
print(IP('192.168.1.1').int())
print(IP('192.168.1.1').strBin())
print(IP('192.168.1.1').strHex())

print('\n反向解析')
print(IP('127.0.0.1').reverseName())

print('\nIP类型')
print(IP('1.2.3.4').iptype())
print(IP('127.5.5.5').iptype())
print(IP('255.255.255.255').iptype())

print('\n判断IP或网段是否包含于另一网段')
print('192.168.1.1' in IP('192.168.1.0/24'))
print('192.168.1.0/28' in IP('192.168.1.0/24'))

print('\n判断IP段是否重叠')
print(IP('192.168.1.0/24').overlaps('192.168.1.0/28'))

print('\n地址比较')
print(IP('192.168.1.0/24') > IP('172.17.0.0/16'))

print('\nIP地址聚合')
a1 = IP('192.168.1.192/26')
a2 = IP('192.168.1.160/27')
a3 = IP('192.168.1.224/27')
print(IPSet([a1, a2, a3]))
