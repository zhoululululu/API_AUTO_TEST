# -*- coding: utf-8 -*-
# @File  : API_test.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


import requests
import unittest
from Log.GetLog import GetLog
import json

class ApiTest(unittest.TestCase):

    def __init__(self):
        log = GetLog.get_log()

    def api_test(method, url, params):
        response = requests.request(method, url, json=json.dumps(params))
        print(response.json())
