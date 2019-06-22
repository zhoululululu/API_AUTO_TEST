# -*- coding: utf-8 -*-
# @File  : test_Login.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :

import unittest

from HTMLTestRunner import HTMLTestRunner

from Common.RunCase import RunCase
import os
import sys
import unittest
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Test_Login(unittest.TestCase):

    def test_Login(self):
        '''验证登录接口'''
        RunCase.run_case(self, "Login")

    def test_2(self):
        Test_Login.test_Login(self)


def Add_case():
    test_dir = rootPath + '\Case'
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_Login.py', top_level_dir=None)
    for test_suit in discover:
        for case in test_suit:
            suit.addTest(case)
    return suit


alllcase = Add_case()
now = time.strftime('%y_%m_%d-%H_%M_%S')
filename = rootPath + '\Report' + '\\' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(alllcase)

if __name__ == '__main__':
    suit = unittest.TestSuite
    runner = unittest.TextTestRunner
    runner.run(suit)
