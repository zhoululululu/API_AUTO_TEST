# -*- coding: utf-8 -*-
# @File  : getCookie.py
# @Author: 周璐
# @Date  : 2019/6/14
# @Desc  :


from common.getAPI import GetAPI
from common.getData import GetData
from common.runMethod import RunMethod
import requests

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

# testcase = GetCookie()
# testcase.get_cookie()
