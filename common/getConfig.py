# -*- coding: utf-8 -*-
# @File  : getConfig.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  : 提取case及API Excel数据

import os
import xlrd

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class Config:

    # 提取Case文件描述内容
    def get_description(self, filename):
        file = open(rootPath + "\\data\\case\\" + filename + ".txt", "r", encoding="utf-8-sig")
        description_row = []
        # 提取描述内容
        for line in file.readlines():
            line = line.strip("\n")
            description_row.append(line.split("|")[0])
        file.close()
        return description_row

    # 提取Case文件param内容
    def get_case_params(self, filename):
        file = open(rootPath + "\\data\\case\\" + filename + ".txt", "r", encoding="utf-8-sig")
        data_row = []
        # 提取param内容
        for line in file.readlines():
            line = line.strip("\n")
            data_row.append(line.split("|")[1])
        file.close()
        return data_row

    # 提取Case文件预期结果内容
    def get_expected_results(self, filename):
        file = open(rootPath + "\\data\\case\\" + filename + ".txt", "r", encoding="utf-8-sig")
        expected_results_row = []
        # 提取预期结果内容
        for line in file.readlines():
            line = line.strip("\n")
            expected_results_row.append(line.split("|")[2])
        file.close()
        return expected_results_row

    # 提取API文件内容
    def get_api_data(self):
        api_book = xlrd.open_workbook(rootPath + "\\data\\API_Data.xlsx")

        # 提取API参数内容等
        api_sheet = api_book.sheet_by_name("API_Data")
        data_row = []
        for i in range(1, api_sheet.nrows):
            rows = api_sheet.row_values(i)
            data_row.append(rows)
        # print(data_row)
        return data_row

    # 提取Case文件下所有的case文件名
    def get_case_name(case_dir):
        case_name = []
        path = rootPath + "\\" + case_dir
        print(path)
        for now_dir, sb_dir, files in os.walk(path, topdown=False):
            for name in files:
                case_name.append((os.path.splitext(name))[0].split("_"))  # 分离文件名及后缀 去除model及func
        return case_name