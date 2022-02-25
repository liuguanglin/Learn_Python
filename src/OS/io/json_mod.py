#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

os.chdir('res')

data_dict = {'name': '张三', 'age': 25, 'is_marriage': False, 'address': {'city': 'Shanghai', 'street': 'Nanjing Road'},
             'hobbies': ['吹', '拉', '弹', '唱']}

json_dump = json.dumps(data_dict)
print('Dump data=>\n', json_dump)

json_pretty = json.dumps(data_dict, ensure_ascii=False, indent=4)
print(f'\nPretty json=>\n{json_pretty}')

data_load = json.loads(json_dump)
print(f"\nGet value: {data_load['address']['street']}")


with open('test.json', 'w') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4, sort_keys=True)

print('\nLoad json data from a file=>')
with open('test.json') as f:
    print(json.load(f))
