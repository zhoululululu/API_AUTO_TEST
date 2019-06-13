# -*- coding: utf-8 -*-
# @File  : GetAPI.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


from Data.Config import Config


class GetAPI():

    def collect_data(self, model=None, api_func=None):
        all_api_data = Config.get_api_data(self)
        api_data = []
        for i in range(len(all_api_data)):
            if all_api_data[i][1] == model and all_api_data[i][2] == api_func:
                api_data = all_api_data[i]
        return api_data

    def get_host(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        host = all_api_data[0]
        return host

    def get_model(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        model = all_api_data[1]
        return model

    def get_api_func(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        api_func = all_api_data[2]
        return api_func

    def get_path(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        path = all_api_data[3]
        return path

    def get_method(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        method = all_api_data[4]
        return method

    def get_data_type(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        data_type = all_api_data[5]
        return data_type

    def get_required_params(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        required_params = all_api_data[6]
        return required_params

    def get_selective_params(self, model=None, api_func=None):
        all_api_data = GetAPI.collect_data(self, model, api_func)
        selective_params = all_api_data[7]
        return selective_params


test = GetAPI()
test.get_required_params("Logout","Logout")