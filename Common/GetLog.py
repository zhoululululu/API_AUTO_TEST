# -*- coding: utf-8 -*-
# @File  : GetLog.py
# @Author: 周璐
# @Date  : 2019/5/28
# @Desc  :

import logging
import time

class GetLog:

    def __init__(self):
        curTime = time.strftime('%Y-%m-%d')
        self.logname = 'Reports/Log/' + 'AutoTest' + '_' + curTime + '.log'

    def get_log(self,level,msg):

        # 创建日志收集器
        logger = logging.getLogger()
        logger.setLevel('DEBUG')

        # 创建handler
        fh = logging.FileHandler(self.logname,'a',encoding='gbk')
        fh.setLevel('INFO')
        ch = logging.StreamHandler()
        ch.setLevel('INFO')

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - 日志信息： %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)


        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def log_debug(self,msg):
        self.get_log('DEBUG',msg)

    def log_info(self,msg):
        self.get_log('INFO',msg)

    def log_warning(self,msg):
        self.get_log('WARNING',msg)

    def log_error(self,msg):
        self.get_log('ERROR',msg)

    def log_critical(self,msg):
        self.get_log('CRITICAL',msg)