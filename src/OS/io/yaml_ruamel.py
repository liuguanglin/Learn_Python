#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from ruamel import yaml
import json

"""
ruamel.yaml是PyYAML的衍生版本，支持YAML 1.2，二者的基本操作相似。
"""

os.chdir('res')

yaml_src_file = 'demo.yml'
json_src_file = 'test.json'
yaml_dst_file = 'j2y.yml'
json_dst_file = 'y2j.yml'


def json_to_yaml(src_file, dst_file):
    with open(src_file, encoding='utf-8') as f:
        data = json.load(f)
    print('JSON data:\n', data)
    with open(dst_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, yaml.RoundTripDumper, allow_unicode=True)
    print('\nYAML data:')
    print(yaml.dump(data, Dumper=yaml.RoundTripDumper, allow_unicode=True))
    print('Convert json to yaml done.')


def yaml_to_json(src_file, dst_file):
    with open(src_file, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    with open(dst_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('Convert yaml to json done.')


json_to_yaml(json_src_file, yaml_dst_file)
yaml_to_json(yaml_src_file, json_dst_file)
