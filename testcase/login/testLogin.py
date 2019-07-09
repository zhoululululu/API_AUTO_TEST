# -*- coding: utf-8 -*-
# @File  : testLogin.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :


from common.runCase import RunCase
import unittest


class TestLogin(unittest.TestCase):

    def test_login(self):
        '''验证登录接口'''
        RunCase.run_case(self, "Login_Login")
