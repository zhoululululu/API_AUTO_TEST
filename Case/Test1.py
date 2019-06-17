# -*- coding: utf-8 -*-
# @File  : Test1.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


from Common.RunMethod import RunMethod
from Data.GetAPI import GetAPI
from Data.GetParams import GetParams
from Data.Config import Config
import os
import sys
import time
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

sys.path.append(rootPath)
from HTMLTestRunner import HTMLTestRunner

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class Test1(unittest.TestCase):

    def test(self):
        case_name = Config.get_case_name(self, "Case")
        for i in range(len(case_name)):
            api_model = case_name[i][0]
            api_func = case_name[i][1]
            param = GetParams.translation_params(self, api_model, api_func)
            method = GetAPI().get_method(api_model, api_func)
            url = GetAPI().get_host(api_model, api_func) + GetAPI().get_path(api_model, api_func)
            data_type = GetAPI().get_data_type(api_model, api_func)

            if len(param) != 0:
                for i in range(len(param)):
                    res = RunMethod().run_main(url, method, eval(param[i]), data_type)
                    print("-----------", res)
            else:
                res = RunMethod().run_main(url, method, param, data_type)
                print("-----------", res)


if __name__ == '__main__':
    suit = unittest.TestSuite
    runner = unittest.TextTestRunner
    runner.run(suit)
