# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: 周璐
# @Date  : 2019/6/22
# @Desc  :


from HTMLTestRunner import HTMLTestRunner

from Common.Config import Config
import os
import sys
import time
import unittest
from Common.RunCase import RunCase

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Test_Login(unittest.TestCase):
    res = [0, 100, 200, 300]


    def main_function(a):
        if a % 3 == 0:
            return a

    def test(self):
        ts = [lambda x=Test_Login.res[i], y=Test_Login.res[i + 1]: [Test_Login.main_function(a) for a in range(x, y) if
                                                                    Test_Login.main_function(a) != None] for i, v in
              enumerate(Test_Login.res) if i < len(Test_Login.res) - 1]

        for t in ts:
            print(t())



    case_num = Config.get_case_name(".\Data\Case")
    # print(case_num)

    def Login(self, case):
        # print(case)
        '''验证接口'''
        RunCase.run_case(self, case)
        return True

    def e1(self, case):
        for i, v in enumerate(case):
            i=i+1
            return i

    def test_Login(self):
        ts = [lambda x=Test_Login.case_num[i], y=Test_Login.case_num[i + 1]: [Test_Login.Login(self, case) for case in
                                                                              (x,y)] for
              i, v in
              enumerate(Test_Login.case_num) if
              i < len(Test_Login.case_num) - 1]

        print("========", ts)
        for t in ts:
            '''验证登录接口111'''
            print("*************")
            print(t())
            print("-------------")


#
def Add_case():
    test_dir = rootPath + '\Common'
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test.py', top_level_dir=None)
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

# test = Test_Login()
# test.Login()
# test.test()
