# -*- coding: utf-8 -*-
# @File  : runMethod.py
# @Author: 周璐
# @Date  : 2019/5/29
# @Desc  : 封装发送接口函数

import requests


class RunMethod:
    def __init__(self):
        self.response = None

    def post_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.post(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.post(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.post(url=url, json=data, **kwargs)
        elif data_type == "file":
            self.response = requests.post(url=url, file=data, **kwargs)
        elif data_type == "-":
            self.response = requests.post(url=url)
        return self.response

    def get_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.get(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.get(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.get(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = requests.get(url=url)
        return self.response

    def put_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.put(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.put(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.put(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = requests.put(url=url)
        return self.response

    def delete_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.delete(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.delete(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.delete(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = requests.delete(url=url)
        return self.response

    def patch_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.patch(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.patch(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.patch(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = requests.patch(url=url)
        return self.response

    def head_main(self, url, data=None, data_type=None, **kwargs):
        if data_type == "params":
            self.response = requests.head(url=url, params=data, **kwargs)
        elif data_type == "data":
            self.response = requests.head(url=url, data=data, **kwargs)
        elif data_type == "json":
            self.response = requests.head(url=url, json=data, **kwargs)
        elif data_type == "-":
            self.response = requests.head(url=url)
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
