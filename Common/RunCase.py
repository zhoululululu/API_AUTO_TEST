# -*- coding: utf-8 -*-
# @File  : RunCase.py
# @Author: 周璐
# @Date  : 2019/6/21
# @Desc  :


from Common.RunMethod import RunMethod
from Common.GetAPI import GetAPI
from Common.GetData import GetData
from Common.Config import Config
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Common.Logging import Logging


class RunCase:

    def run_case(self, case):
        '''验证是否登录成功'''
        # case_name = Config.get_case_name("\\Data\Case\\" + case+".txt")
        # print(case_name)
        # for i in range(len(case_name)):
        #     api_model = case_name[i][0]
        #     api_func = case_name[i][1]
        #     description = Config.get_description(self, api_model + "_" + api_func)
        #     param = GetData.translation_params(self, api_model, api_func)
        #     method = GetAPI().get_method(api_model, api_func)
        #     url = GetAPI().get_host(api_model, api_func) + GetAPI().get_path(api_model, api_func)
        #     data_type = GetAPI().get_data_type(api_model, api_func)
        #     expected_results = Config.get_expected_results(self, api_model + "_" + api_func)
        #
        #     if len(param) != 0:
        #         for i in range(len(param)):
        #             res = RunMethod().run_main(url, method, eval(param[i]), data_type)
        #             print(description, res.json())
        #             self.assertTrue(description, res.json().get("code") == expected_results[i])
        #
        #     else:
        #         res = RunMethod().run_main(url, method, param, data_type)
        #         print(description, res.json())
        #         self.assertTrue(description, res.json().get("code") == expected_results[0])

        case_name = case.split("_")
        api_model = case_name[0]
        api_func = case_name[1]
        description = Config.get_description(self, api_model + "_" + api_func)
        param = GetData.translation_params(self, api_model, api_func)
        method = GetAPI().get_method(api_model, api_func)
        url = GetAPI().get_host(api_model, api_func) + GetAPI().get_path(api_model, api_func)
        data_type = GetAPI().get_data_type(api_model, api_func)
        expected_results = Config.get_expected_results(self, api_model + "_" + api_func)

        if len(param) != 0:

            for i in range(len(param)):
                res = RunMethod().run_main(url, method, eval(param[i]), data_type)
                print(description[i], res.json())
                self.assertTrue(res.json().get("code") == expected_results[i])

        else:
            res = RunMethod().run_main(url, method, param, data_type)
            print(description[0], res.json())
            self.assertTrue(res.json().get("code") == expected_results[0])
