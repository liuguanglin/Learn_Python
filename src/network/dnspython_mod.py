#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dns import resolver

print('A record')
my_resolver = resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8', '64.6.64.6']  # 可指定DNS服务器
ans_a = my_resolver.resolve('m.root-servers.net', 'A')
for i in ans_a:
    print(i)

print('\nAAAA record')
ans_aaaa = resolver.resolve('bii.dns-lab.net', 'AAAA')
for i in ans_aaaa:
    print(i)

print('\nNS record')
ans_ns = resolver.resolve('mozilla.org', 'NS')
for i in ans_ns:
    print(i)

print('\nCNAME record')
ans_cname = resolver.resolve('www.mozilla.org', 'CNAME')
for i in ans_cname:
    print(i)

print('\nMX record')
ans_mx = resolver.resolve('kernel.org', 'MX')
for i in ans_mx:
    print(i)

print('\nPTR record')
ans_ptr = resolver.resolve('217.84.178.139.in-addr.arpa', 'PTR')
for i in ans_ptr:
    print(i)
