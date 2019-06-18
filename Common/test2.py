# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: 周璐
# @Date  : 2019/6/18
# @Desc  :
# -*- coding: utf-8 -*-
# @File  : Test1.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


from Common.RunMethod import RunMethod
from Data.GetAPI import GetAPI
from Data.GetData import GetData
from Data.Config import Config
import os
import sys
import unittest
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from HTMLTestRunner import HTMLTestRunner


class Test2(unittest.TestCase):

    # @staticmethod
    def f1(self, url, method, param, data_type, expected_results):
        '''验证是否登录成功'''
        res = RunMethod().run_main(url, method, param, data_type)
        self.assertTrue(res.json().get("code") == expected_results)
        return res

    def f2(self, url, method, param, data_type, expected_results):
        '''验证是否登录成功'''
        res = RunMethod().run_main(url, method, param, data_type)
        self.assertTrue(res.json().get("code") == expected_results)

        return res

    def test_f11(self):
        '''验证是否登录成功'''
        case_name = Config.get_case_name(".\Case")
        for i in range(len(case_name)):
            api_model = case_name[i][0]
            api_func = case_name[i][1]
            param = GetData.translation_params(self, api_model, api_func)
            method = GetAPI().get_method(api_model, api_func)
            url = GetAPI().get_host(api_model, api_func) + GetAPI().get_path(api_model, api_func)
            data_type = GetAPI().get_data_type(api_model, api_func)
            expected_results = Config.get_expected_results(self, api_model + "_" + api_func)

            if len(param) != 0:
                for i in range(len(param)):
                    res = Test2.f1(self, url, method, eval(param[i]), data_type, expected_results[i])
                    print("-----------", res.json(), res.json().get("code"))

            else:
                res = Test2.f2(self, url, method, param, data_type, expected_results[0])
                print("-----------", res.json(), res.json().get("code"))


test = Test2()
test.test_f11()

def Add_case(self):
    test_dir = rootPath + '\Common'
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py', top_level_dir=None)
    print(discover)
    for test_suit in discover:
        for case in test_suit:
            suit.addTest(case)
    return suit


alllcase =Add_case()
now = time.strftime('%y_%m_%d-%H_%M_%S')
filename = rootPath + '\Report' + '\\' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(alllcase)

Add_case()
if __name__ == '__main__':
    suit = unittest.TestSuite
    runner = unittest.TextTestRunner
    runner.run(suit)