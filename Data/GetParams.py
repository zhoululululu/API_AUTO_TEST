# -*- coding: utf-8 -*-
# @File  : GetParams.py
# @Author: 周璐
# @Date  : 2019/5/31
# @Desc  :


from Data.GetAPI import GetAPI
from Data.Config import Config


class GetParams:

    def translation_params(self, model, api_func):
        api_param = []
        data_param = [] #API参数
        param = {}
        trans_params = []

        required_params = GetAPI.get_required_params(self, model, api_func)
        selective_params = GetAPI.get_selective_params(self, model, api_func)
        params_data = Config.get_case_params(self, api_func)

        if required_params == "-" and selective_params == "-":
            return trans_params

        elif required_params != "-" and selective_params == "-":
            # 先将API参数组合为list
            pa = str(required_params).split(",")
            for i in range(len(pa)):
                param[pa[i]] =""
            data_param.append(param)
            # print(data_param)

            for j in range(len(params_data)):
                print(data_param[j])

                # param = params_data[j].split(",")
                # print(param)
                # data_param.insert(j,param)

        return data_param
test = GetParams()
test.translation_params("Login", "Login")
# test.translation_params("Logout","Logout")
# test.translation_params("-","-")
