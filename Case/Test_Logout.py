# -*- coding: utf-8 -*-
# @File  : Test_Logout.py
# @Author: 周璐
# @Date  : 2019/6/20
# @Desc  :

from Common.RunCase import RunCase
import unittest


class Test_Logout(unittest.TestCase):

    def test_logout(self):
        """验证登出接口"""
        RunCase.run_case(self, "Logout_Logout")
