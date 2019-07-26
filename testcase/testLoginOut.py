# -*- coding: utf-8 -*-
# @File  : testLoginOut.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :


from common.runCase import RunCase
import unittest


class TestLoginOut(unittest.TestCase):

    def test_login(self):
        '''验证登录接口'''
        RunCase.run_case(self, "Login_Login")

    def test_logout(self):
        '''验证登出接口'''
        RunCase.run_case(self, "Logout_Logout")
