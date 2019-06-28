# -*- coding: utf-8 -*-
# @File  : AllRun.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


import os
import sys
import time
import unittest
from Run.HTMLTestRunner_cn import HTMLTestRunner

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class AllRun(unittest.TestCase):

    def add_case(self):
        test_dir = rootPath + '\Case'
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*.py', top_level_dir=None)
        for test_suit in discover:
            for case in test_suit:
                suit.addTest(case)
        return suit


test = AllRun()
alllcase = test.add_case()
now = time.strftime('%y_%m_%d-%H_%M_%S')
filename = rootPath + '\Report' + '\\' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(alllcase)

run = AllRun()
run.add_case()
