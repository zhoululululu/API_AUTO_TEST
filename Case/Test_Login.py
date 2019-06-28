# -*- coding: utf-8 -*-
# @File  : Test_Login.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :


from Common.RunCase import RunCase
import unittest


class Test_Login(unittest.TestCase):

    def test_Login(self):
        '''验证登录接口'''
        RunCase.run_case(self, "Login_Login")
