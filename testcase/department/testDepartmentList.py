# -*- coding: utf-8 -*-
# @File  : testDepartmentList.py
# @Author: 周璐
# @Date  : 2019/7/9
# @Desc  :


from common.runCase import RunCase
import unittest
from common.getCookie import GetCookie


class TestDepartmentList(unittest.TestCase):

    def test_department_list(self):
        '''验证登录接口'''
        RunCase.run_case(self, "PlatformConfigDepartment_DepartmentList", headers=GetCookie.get_cookie(self))


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest()
