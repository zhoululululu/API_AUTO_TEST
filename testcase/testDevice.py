# -*- coding: utf-8 -*-
# @File  : testDevice.py
# @Author: 周璐
# @Date  : 2019/7/26
# @Desc  :

from common.runCase import RunCase
import unittest


class TestDevice(unittest.TestCase):

    def test_device_list(self):
        '''验证查询固件版本接口'''
        RunCase.run_case(self, "Device_List")
