# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 11:57
# @Author  : cap
# @FileName: test.py
# @Software: PyCharm Community Edition
# import csv
#
# csvfile = open('../../data/chp3/data-text.csv','r')
# reader = csv.reader(csvfile)
# # reader = csv.DictReader(csvfile)
#
# for row in reader:
#     print(row)

# import json
#
# json_data = open('../../data/chp3/data-text.json').read()
#
# data = json.loads(json_data)
#
# for item in data:
#     print(item)

from xml.etree import ElementTree as ET

tree = ET.parse('../../data/chp3/data-text.xml')
root = tree.getroot()

data = root.find('Data')

all_data = []

for observation in data:
    record = {}
    for item in observation:
        print(list(item))
        item_list = list(item.attrib.keys())
        lookup_key = item_list[0]

        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']

        record[rec_key] = rec_value

    all_data.append(record)

# print(all_data)
print(len(all_data))
print(dir(root))
print(list(data))
print(len(list(data)))