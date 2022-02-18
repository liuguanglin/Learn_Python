#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os

os.chdir('res')
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['姓名', '性别', '年龄'])
    data = []
    with open('csv.txt', 'r', encoding='utf-8') as txtfile:
        while True:
            txt_line = txtfile.readline().strip('\r\n')
            if not txt_line:
                break
            txt_lst = txt_line.split(',')
            field0 = txt_lst[0]
            field1 = txt_lst[1]
            field2 = txt_lst[2]
            data.append((field0, field1, field2))

    writer.writerows(data)

with open('test.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)

with open('test.csv', 'w', newline='') as csvfile:
    fields = ['姓名', '性别', '年龄']
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    data = []
    with open('csv.txt', 'r', encoding='utf-8') as txtfile:
        while True:
            data_line = {}
            txt_line = txtfile.readline().strip('\r\n')
            if not txt_line:
                break
            txt_lst = txt_line.split(',')
            data_line[fields[0]] = txt_lst[0]
            data_line[fields[1]] = txt_lst[1]
            data_line[fields[2]] = txt_lst[2]
            data.append(data_line)

    writer.writerows(data)

print('\nDictReader()')
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
