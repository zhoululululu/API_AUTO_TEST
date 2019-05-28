# -*- coding: utf-8 -*-
# @File  : Test1.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :

from Common.API_test import ApiTest

param = {"loginname":"superAdmin","password":"123456"}

ApiTest.api_test("post","http://117.50.57.155:48230/user/login",param)
