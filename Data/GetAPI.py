# -*- coding: utf-8 -*-
# @File  : GetAPI.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


import xlrd
import os
import logging
import unittest


class GetAPI():

    def __init__(self):
        # 设置API_Data路径
        API_Excel = os.path.join(".\API_Data.xlsx")

        # 打印sheet的名字
        self.workbook = xlrd.open_workbook(API_Excel)

    def getData(self):
        # 根据sheet名称获取sheet内容,sheet行数,sheet列数
        API_sheet = self.workbook.sheet_by_name("API_Data")
        print(API_sheet.name)
        rowNum = API_sheet.nrows
        colNum = API_sheet.ncols

        rows = API_sheet.row_values(0)
        print(rows)

        collist = []
        for i in range(colNum):
            cols = API_sheet.col_values()
            collist.append(cols)
        print(collist)

test = GetAPI()
test.getData()