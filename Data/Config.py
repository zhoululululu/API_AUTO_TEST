# -*- coding: utf-8 -*-
# @File  : GetAPI.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :


import configparser
import os


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ParamsData.txt')
        self.config.read(self.conf_path, encoding='UTF-8')

        self.conf = {}

    def get_conf(self):
        #Login
        self.conf['user'] = self.config.get("Login", "user")
        self.conf['password'] = self.config.get("Login", "password")

        return self.conf
