# -*- coding: utf-8 -*-
# @File  : GetAPI.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :

import os
import xlrd
import string

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class Config:

    # 提取Case文件内容
    def get_case_params(self, filename):
        file = open(rootPath + "\\Case\\" + filename + ".txt", "r", encoding="utf-8-sig")
        data_row = []
        # 提取测试描述及参数
        for line in file.readlines():
            line = line.strip("\n")
            data_row.append(line.split("|")[1])
        return data_row

    # 提取API文件内容
    def get_api_data(self):
        api_book = xlrd.open_workbook(rootPath + "\\Data\\API_Data.xlsx")

        # 提取API参数内容等
        api_sheet = api_book.sheet_by_name("API_Data")
        data_row = []
        for i in range(1, api_sheet.nrows):
            rows = api_sheet.row_values(i)
            data_row.append(rows)
        # print(data_row)
        return data_row

    # 提取Case文件下所有的case文件名
    def get_case_name(self, case_dir):
        case_name = []
        path = rootPath + "\\" + case_dir
        for now_dir, sb_dir, files in os.walk(path, topdown=False):
            for name in files:
                case_name.append((os.path.splitext(name))[0].split("_"))  # 分离文件名及后缀 去除model及func
        return case_name

