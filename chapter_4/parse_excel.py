# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 9:05
# @Author  : cap
# @FileName: parse_excel.py
# @Software: PyCharm Community Edition

import xlrd
import pprint

book = xlrd.open_workbook('../data/chp4/SOWC 2014 Stat Tables_Table 9.xlsx')

# sheet_name = book.sheets()
# for sheet in sheet_name:
#     print(sheet.name)
sheet = book.sheet_by_name('Table 9 ')

# for d in dir(sheet):
#     print(d)
print(sheet.nrows)

rows = sheet.nrows
count = 0
data = {}

for i in range(14,rows):
    # print(sheet.row_values(i))
    row = sheet.row_values(i)
    # for cell in row:
    #     print(cell)
    country = row[1]
    data[country] = {
        'child_labor':{
            'total':[row[4],row[5]],
            'male':[row[6],row[7]],
            'female':[row[8],row[9]]
        },
        'child_marrage':{
            'married_by_15':[row[10],row[11]],
            'married_by_18':[row[12],row[13]]
        }
    }

    if country == 'Zimbabwe':
        break
    # print(i,row)
    # count = count + 1

# print(data['Afghanistan']['child_labor'])
pprint.pprint(data)