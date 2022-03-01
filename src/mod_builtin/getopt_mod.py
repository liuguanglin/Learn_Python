#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import sys

options, arg = getopt.getopt(sys.argv[1:], 'u:p:', ['user=', 'pass='])
try:
    for name, value in options:
        if name in ('-u', '--user'):
            print(f'user: {value}')
        if name in ('-p', '--pass'):
            print(f'password: {value}')
except getopt.GetoptError:
    print('Invaid input.')
