# -*- coding: utf-8 -*-
# @File  : GetCookie.py
# @Author: 周璐
# @Date  : 2019/6/14
# @Desc  :


from Data.GetAPI import GetAPI
from Data.GetParams import GetParams
import requests


class GetCookie:

    def get_cookie(self):
        param = GetParams.translation_params(self, "Login", "Login")
        method = GetAPI().get_method("Login", "Login")
        url = GetAPI().get_host("Login", "Login") + GetAPI().get_path("Login", "Login")
        data_type = GetAPI().get_data_type("Login", "Login")
        s = requests.Session()
        print (eval(param[0]))
        res = s.post(url, eval(param[0]))
        cookies = res.cookies.get_dict()
        print("-----------", res.json())
        print(cookies)

        # print(res.headers)
        # print(s.headers)


test = GetCookie()
test.get_cookie()
