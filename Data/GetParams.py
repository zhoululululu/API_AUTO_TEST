# -*- coding: utf-8 -*-
# @File  : GetParams.py
# @Author: 周璐
# @Date  : 2019/5/31
# @Desc  :


from Data.GetAPI import GetAPI


class GetParams:
    def translation_params(self, model, api_func):
        params = ""
        required_params = GetAPI.get_required_params(self, model, api_func)
        selective_params = GetAPI.get_selective_params(self, model, api_func)
        if required_params == "-" and selective_params == "-":
            return params
        elif required_params != "-" and selective_params == "-":
            return params

        print(required_params, selective_params)
        # all_case_data = Config.get_case_params(self, fileName)
        # for i in range (len(all_case_data)):
        #     params = all_case_data[i][1]
        #     print(params)
        # print(all_case_data)


test = GetParams()
test.translation_params("Login", "Login")
# test.translation_params("Logout","Logout")
# test.translation_params("-","-")
