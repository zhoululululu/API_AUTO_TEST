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
        data_param = []
        param = {}
        trans_params = []

        required_params = GetAPI.get_required_params(self, model, api_func)
        selective_params = GetAPI.get_selective_params(self, model, api_func)
        params_data = Config.get_case_params(self, api_func)
        print(params_data)

        if required_params == "-" and selective_params == "-":
            return trans_params

        elif required_params != "-" and selective_params == "-":
            pa = str(required_params).split(",")
            # d_pa = str(params_data).split(",")
            print(pa)
            # print(d_pa)
            for i in range(len(pa)):
                param[pa[i]] = ""
                for j in range(len(params_data)):
                    print((params_data[j].split(",")))
                    param[pa[i]] = params_data[j].split(",")[i]
                    data_param.append(param)
            print(data_param)
            return trans_params

        print(required_params, selective_params)
        # all_case_data = Config.get_case_params(self, fileName)
        # for i in range (len(all_case_data)):
        #     params = all_case_data[i][1]
        #     print(params)
        # print(all_case_data)


test = GetParams()
# test.get_params("Login", "Login")
test.translation_params("Login", "Login")
# test.translation_params("Logout","Logout")
# test.translation_params("-","-")
