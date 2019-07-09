# -*- coding: utf-8 -*-
# @File  : testLogout.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :

from common.runCase import RunCase
import unittest


class TestLogout(unittest.TestCase):

    def test_logout(self):
        """验证登出接口"""
        RunCase.run_case(self, "Logout_Logout")
