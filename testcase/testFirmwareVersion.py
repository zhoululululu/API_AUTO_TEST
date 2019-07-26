# -*- coding: utf-8 -*-
# @File  : testFirmwareVersion.py
# @Author: 周璐
# @Date  : 2019/7/26
# @Desc  :


from common.runCase import RunCase
import unittest


class TestFirmwareVersion(unittest.TestCase):

    def test_firmwareVersion_list(self):
        '''验证查询固件版本接口'''
        RunCase.run_case(self, "FirmwareVersion_List")

    # def test_firmwareVersion_add(self):
    #     '''验证新增固件版本接口'''
    #     RunCase.run_case(self, "FirmwareVersion_Add")
