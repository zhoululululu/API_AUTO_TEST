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
        f = file.readlines()
        data_row = []
        # 提取测试描述及参数
        for i in range(len(f)):
            data = f[i].split("|")
            data_row.append(data)
        return data_row

    # 提取API文件内容
    def get_api_data(self):
        apibook = xlrd.open_workbook(rootPath + "\\Data\\API_Data.xlsx")

        # 提取API参数内容等
        API_sheet = apibook.sheet_by_name("API_Data")
        data_row = []
        for i in range(1, API_sheet.nrows):
            rows = API_sheet.row_values(i)
            data_row.append(rows)
        #print(data_row)
        return data_row
