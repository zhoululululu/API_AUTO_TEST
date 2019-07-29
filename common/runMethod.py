# -*- coding: utf-8 -*-
# @File  : runMethod.py
# @Author: 周璐
# @Date  : 2019/5/29
# @Desc  : 封装发送接口函数

import requests
from common.getConfig import IniConfig
from common.getLogging import Logging


class RunMethod:

    def __init__(self):

        self.logging = Logging()
        self.response = None
        self.session = requests.session()
        self.config = IniConfig()
        self.c = self.config.get_conf()
        self.session.headers = RunMethod.header(self)

    def take_authorization(self):
        authorization = requests.post("http://117.50.57.155:48230/user/login",
                                      json={'loginname': 'zhoulu', 'password': '123456'}).headers["Authorization"]
        IniConfig().set_authorization(authorization)
        self.logging.info("已登录获取Authorization")
        self.logging.info("Authorization ：" + authorization)

    def header(self):
        hd = {"Content-Type": self.c["Content-Type"],
              "Authorization": self.c["Authorization"]}
        return hd

    def post_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.post(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.post(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.post(url=url, json=data, **kwargs)
        elif data_type == "file":
            self.response = self.session.post(url=url, file=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.post(url=url)
        return self.response

    def get_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.get(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.get(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.get(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.get(url=url)
        return self.response

    def put_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.put(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.put(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.put(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.put(url=url)
        return self.response

    def delete_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.delete(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.delete(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.delete(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.delete(url=url)
        return self.response

    def patch_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.patch(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.patch(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.patch(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.patch(url=url)
        return self.response

    def head_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = self.session.head(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = self.session.head(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = self.session.head(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = self.session.head(url=url)
        return self.response

    def run_main(self, url, method, data=None, data_type=None, **kwargs):
        if method == "post":
            self.response = self.post_main(url, data, data_type, **kwargs)
        elif method == "get":
            self.response = self.get_main(url, data, data_type, **kwargs)
        elif method == "put":
            self.response = self.put_main(url, data, data_type, **kwargs)
        elif method == "options":
            self.response = self.options_main(url, data, data_type, **kwargs)
        elif method == "patch":
            self.response = self.patch_main(url, data, data_type, **kwargs)
        elif method == "delete":
            self.response = self.delete_main(url, data, data_type, **kwargs)
        else:
            self.response = self.head_main(url, data, data_type, **kwargs)
        return self.response
