# -*- coding: utf-8 -*-
# @File  : runCase.py
# @Author: 周璐
# @Date  : 2019/6/21
# @Desc  : 调取case，组装APi所需各个字段再调用runmethod


from common.runMethod import RunMethod
from common.getAPI import GetAPI
from common.getData import GetData
from common.getConfig import Config
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class RunCase:

    def run_case(self, case, **kwargs):
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
                res = RunMethod().run_main(url, method, eval(param[i]), data_type, **kwargs)
                print(description[i], res.json()["code"], res.json()["msg"])
                self.assertTrue(res.json().get("code") == expected_results[i])

        else:
            res = RunMethod().run_main(url, method, param, data_type, **kwargs)
            print(description[0], res.json()["code"], res.json()["msg"])
            self.assertTrue(res.json().get("code") == expected_results[0])
