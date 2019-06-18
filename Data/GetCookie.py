# -*- coding: utf-8 -*-
# @File  : GetCookie.py
# @Author: 周璐
# @Date  : 2019/6/14
# @Desc  :


from Data.GetAPI import GetAPI
from Data.GetData import GetData
import requests
from Common.RunMethod import RunMethod


class GetCookie:
    def __init__(self):
        self.session = requests.session()

    def get_cookie(self):
        param = GetData.translation_params(self, "Login", "Login")
        method = GetAPI().get_method("Login", "Login")
        url = GetAPI().get_host("Login", "Login") + GetAPI().get_path("Login", "Login")
        data_type = GetAPI().get_data_type("Login", "Login")
        res = RunMethod().run_main(url, method, eval(param[0]), data_type)
        header = res.headers
        return header

# test = GetCookie()
# test.get_cookie()
