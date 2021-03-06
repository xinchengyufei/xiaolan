# -*- coding: utf-8 -*-
# LOG

import sys
import os
import requests
import json
import base64
import logging
import os.path
import time

class Log(object):

    def __init__(self):

        pass

    def get(self, mode):

        if mode == 'all':
            xiaolanlog = open("./more/xiaolan.log", "r")
            log = xiaolanlog.read()
            return log
        else:
            pass

    def add_log(self, log, level):

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/xiaolan/memory_center/more/'
        log_name = log_path + 'xiaolan' + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='r+')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        if level == 'debug':
            logger.debug(log)
        elif level == 'info':
            logger.info(log)
        elif level == 'warning':
            logger.warning(log)
        elif level == 'error':
            logger.error(log)
        elif level == 'critical':
            logger.critical(log)