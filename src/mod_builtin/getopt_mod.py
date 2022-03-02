#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import sys


def usage():
    print("""Usage:
    -h|--help show help
    -u|--user username
    -p|--pass password
    """)


options, arg = getopt.getopt(sys.argv[1:], 'hu:p:', ['help', 'user=', 'pass='])
print(f'options: {options}, arg: {arg}')
try:
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
            exit()
        if name in ('-u', '--user'):
            print(f'user: {value}')
        if name in ('-p', '--pass'):
            print(f'password: {value}')
except getopt.GetoptError:
    print('Invalid input.')
