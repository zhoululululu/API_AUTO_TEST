# -*- coding: utf-8 -*-
# @File  : Test1.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


from Common.RunMethod import RunMethod
from Data.GetAPI import  GetAPI
from Data.Config import  Config

def test():
    run = RunMethod()

    param = {"loginname":"superAdmin","password":"123456"}
    res = run.run_main("post","http://117.50.57.155:48230/user/login",param,"json")
    print (res)
test()
