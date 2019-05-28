# -*- coding: utf-8 -*-
# @File  : GetAPI.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


import os
import sys
import time
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

sys.path.append(rootPath)
from HTMLTestRunner import HTMLTestRunner


class AllRun(unittest.TestCase):

    def Add_case(self):
        test_dir = rootPath + '\Case'
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='*test.py', top_level_dir=None)
        print(discover)
        for test_suit in discover:
            for case in test_suit:
                suit.addTest(case)
        return suit

    alllcase = Add_case()
    now = time.strftime('%y_%m_%d-%H_%M_%S')
    filename = rootPath + '\Report' + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='标准产品平台UI测试报告', description='测试执行情况')
    runner.run(alllcase)

run = AllRun()
run.Add_case()