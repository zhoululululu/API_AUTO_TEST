# -*- coding: utf-8 -*-
# @File  : GetParams.py
# @Author: 周璐
# @Date  : 2019/5/31
# @Desc  :


from Data.GetAPI import GetAPI
from Data.Config import Config


class GetParams:

    def translation_params(self, model, api_func):

        required_params = GetAPI.get_required_params(self, model, api_func)
        selective_params = GetAPI.get_selective_params(self, model, api_func)
        params_data = Config.get_case_params(self, model+"_"+api_func)

        trans_params = []  # 定义拼接参数字典

        if required_params == "-" and selective_params == "-":
            # trans_params.append("{"":""}")
            return trans_params

        elif required_params != "-" and selective_params == "-":
            # 将case与API参数组合为字典
            param = {}  # 定义单组参数值
            pa_required = str(required_params).split(",")  # 取出所有的必填项
            for j in range(len(params_data)):
                for i in range(len(pa_required)):
                    param[pa_required[i]] = params_data[j].strip("'").split(",")[i]  # 拼接api参数
                trans_params.append(str(param))
            return trans_params

        elif selective_params != "-" and required_params == "-":
            # 将case与API参数组合为字典
            param = {}  # 定义单组参数值
            pa_selected = str(selective_params).split(",")  # 取出所有的选填项
            for j in range(len(params_data)):
                for i in range(len(pa_selected)):
                    param[pa_selected[i]] = params_data[j].strip("'").split(",")[i]  # 拼接api参数
                trans_params.append(str(param))
            return trans_params

        elif selective_params != "-" and required_params != "-":
            # 将case与API参数组合为字典
            param = {}  # 定义单组参数值
            pa_required = str(required_params).split(",")  # 取出所有的必填项
            pa_selected = str(selective_params).split(",")  # 取出所有的选填项
            pa_all = pa_required + pa_selected
            for j in range(len(params_data)):
                for i in range(len(pa_all)):
                    param[pa_all[i]] = params_data[j].strip("'").split(",")[i]  # 拼接api参数
                trans_params.append(str(param))
            return trans_params
