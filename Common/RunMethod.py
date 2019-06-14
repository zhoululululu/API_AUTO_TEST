# -*- coding: utf-8 -*-
# @File  : RunMethod.py
# @Author: 周璐
# @Date  : 2019/5/29
# @Desc  : 封装发送接口函数

import requests
import json


class RunMethod:
    def post_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.post(url=url, params=data, cookie=None, headers=header, verify=False)
            elif data_type == "data":
                response = requests.post(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.post(url=url, json=data, headers=header, verify=False)
            elif data_type == "file":
                response = requests.post(url=url, file=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.post(url=url, headers=header, verify=False)
        else:
            if data_type == "params":
                response = requests.post(url=url, params=data, verify=False)
            if data_type == "data":
                response = requests.post(url=url, data=data, verify=False)
            if data_type == "json":
                response = requests.post(url=url, json=data, verify=False)
            elif data_type == "file":
                response = requests.post(url=url, file=data, verify=False)
            elif data_type == "-":
                response = requests.post(url=url)
        return response.json()

    def get_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.get(url=url, params=data, headers=header, verify=False)
            elif data_type == "data":
                response = requests.get(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.get(url=url, json=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.get(url=url, verify=False)
        else:
            if data_type == "params":
                response = requests.get(url=url, params=data, verify=False)
            elif data_type == "data":
                response = requests.get(url=url, data=data, verify=False)
            elif data_type == "json":
                response = requests.get(url=url, json=data, verify=False)
            elif data_type == "-":
                response = requests.get(url=url)
        return response.json()

    def put_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.put(url=url, params=data, headers=header, verify=False)
            elif data_type == "data":
                response = requests.put(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.put(url=url, json=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.put(url=url, verify=False)
        else:
            if data_type == "params":
                response = requests.put(url=url, params=data, verify=False)
            elif data_type == "data":
                response = requests.put(url=url, data=data, verify=False)
            elif data_type == "json":
                response = requests.put(url=url, json=data, verify=False)
            elif data_type == "-":
                response = requests.put(url=url)
        return response.json()

    def delete_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.delete(url=url, params=data, headers=header, verify=False)
            elif data_type == "data":
                response = requests.delete(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.delete(url=url, json=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.delete(url=url, verify=False)
        else:
            if data_type == "params":
                response = requests.delete(url=url, params=data, verify=False)
            elif data_type == "data":
                response = requests.delete(url=url, data=data, verify=False)
            elif data_type == "json":
                response = requests.delete(url=url, json=data, verify=False)
            elif data_type == "-":
                response = requests.delete(url=url)
        return response.json()

    def patch_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.patch(url=url, params=data, headers=header, verify=False)
            elif data_type == "data":
                response = requests.patch(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.patch(url=url, json=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.patch(url=url, verify=False)
        else:
            if data_type == "params":
                response = requests.patch(url=url, params=data, verify=False)
            elif data_type == "data":
                response = requests.patch(url=url, data=data, verify=False)
            elif data_type == "json":
                response = requests.patch(url=url, json=data, verify=False)
            elif data_type == "-":
                response = requests.patch(url=url)
        return response.json()

    def head_main(self, url, data=None, data_type=None, header=None):
        response = None
        if header != None:
            if data_type == "params":
                response = requests.head(url=url, params=data, headers=header, verify=False)
            elif data_type == "data":
                response = requests.head(url=url, data=data, headers=header, verify=False)
            elif data_type == "json":
                response = requests.head(url=url, json=data, headers=header, verify=False)
            elif data_type == "-":
                response = requests.head(url=url, verify=False)
        else:
            if data_type == "params":
                response = requests.head(url=url, params=data, verify=False)
            elif data_type == "data":
                response = requests.head(url=url, data=data, verify=False)
            elif data_type == "json":
                response = requests.head(url=url, json=data, verify=False)
            elif data_type == "-":
                response = requests.head(url=url)
        return response.json()

    def run_main(self, url, method, data=None, data_type=None, header=None):
        response = None
        if method == "post":
            response = self.post_main(url, data, data_type, header)
        elif method == "get":
            response = self.get_main(url, data, data_type, header)
        elif method == "put":
            response = self.put_main(url, data, data_type, header)
        elif method == "options":
            response = self.options_main(url, data, data_type, header)
        elif method == "patch":
            response = self.patch_main(url, data, data_type, header)
        elif method == "delete":
            response = self.delete_main(url, data, data_type, header)
        else:
            response = self.head_main(url, data, data_type, header)
        return json.dumps(response, ensure_ascii=False)
