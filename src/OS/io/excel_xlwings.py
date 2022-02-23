#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwings as xw
import os

os.chdir('res')


def load_data(src_data_file):
    data_list = []
    with open(src_data_file, encoding='utf-8') as f:
        while True:
            txt_line = f.readline().strip('\r\n')
            if not txt_line:
                break
            data_list.append(txt_line.split('\t'))
    return data_list


def write_data(dst_file):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.add()
    print(f'当前工作簿: {app.books.active}')
    curr_sht = wb.sheets.add('成绩表')
    print(f'当前工作表: {wb.sheets.active}')
    # curr_sht = wb.sheets[0]
    wb.sheets[1].delete()

    curr_sht.range('A2').value = load_data('excel.txt')

    second_last_column = curr_sht.range('A2').end('right').get_address(0, 0)[0]
    last_column = chr(ord(second_last_column) + 1)
    last_row = curr_sht.range('A2').end('down').row

    rng_title = curr_sht.range('A1')
    rng_title.value = '学生成绩表'
    rng_title.api.Font.Bold = True  # 字体加粗
    curr_sht.range(f'A1:{last_column}1').api.Merge()  # 合并单元格
    rng_title.api.HorizontalAlignment = -4108  # 居中对齐
    rng_title.row_height = 20  # 行高

    rng_header = curr_sht.range(f'A2:{last_column}2')
    curr_sht.range(f'{last_column}2').value = '平均分'
    rng_header.color = (221, 221, 221)  # 背景色
    rng_header.api.Font.Bold = True
    rng_header.api.HorizontalAlignment = -4108

    rng_all = curr_sht.range(f'A2:{last_column}{last_row}')
    rng_all.api.Borders(7).LineStyle = 1  # 左边框
    rng_all.api.Borders(8).LineStyle = 1  # 顶部边框
    rng_all.api.Borders(9).LineStyle = 1  # 底部边框
    rng_all.api.Borders(10).LineStyle = 1  # 右边框
    rng_all.api.Borders(11).LineStyle = 1  # 内部垂直线
    rng_all.api.Borders(12).LineStyle = 1  # 内部水平线
    rng_avg_score = curr_sht.range(f'E3:E{last_row}')
    rng_avg_score.formula = f'=AVERAGE(A3:{second_last_column}3)'  # 插入公式
    rng_avg_score.api.NumberFormat = '0.0'  # 设置数字格式
    wb.save(dst_file)
    wb.close()
    app.quit()


def read_data(data_file):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(data_file)
    curr_sht = wb.sheets[0]
    last_column = curr_sht.range('A2').end('right').get_address(0, 0)[0]
    last_row = curr_sht.range('A2').end('down').row
    for i in range(3, last_row + 1):
        rng_name = curr_sht.range('A' + str(i))
        rng_avg_score = curr_sht.range(last_column + str(i))
        print(f'{rng_name.value}平均分{round(rng_avg_score.value,1)}')
    wb.close()
    app.quit()


if __name__ == '__main__':
    write_data('test.xlsx')
    read_data('test.xlsx')
