#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

os.chdir('res')

documents = """
---
name: Ivy
age: 18
---
name: 王二牛
age: 25
"""

for data in yaml.load_all(documents, Loader=yaml.SafeLoader):
    print(data)


print('\nData from yaml file:')
with open('demo.yml', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.Loader)
    print(data)

