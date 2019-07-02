# -*- coding:utf-8 -*-
import sys
import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO  # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'  # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = '../logs/logging/spiders.log'  # 默认日志文件名称


class Logger(object):
    def __init__(self):
        self._logger = logging.getLogger()
        self.formatter = logging.Formatter(fmt=DEFAULT_LOG_FMT, datefmt=DEFUALT_LOG_DATEFMT)
        self._logger.addHandler(self._get_file_handler(DEFAULT_LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(DEFAULT_LOG_LEVEL)

    def _get_file_handler(self, filename):
        filehandler = logging.FileHandler(filename, encoding="utf-8")
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger

logger = Logger().logger
